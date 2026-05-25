import os
import json
import pdfplumber
from google import genai
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv

load_dotenv()

# Define the expected JSON structure using Pydantic (Strict Schema)
class LineItem(BaseModel):
    description: str
    quantity: float
    unit_price: float
    total: float

class InvoiceData(BaseModel):
    invoice_number: str
    date: str
    vendor_name: str
    total_amount: float
    line_items: List[LineItem]

def extract_text_from_pdf(pdf_path: str) -> str:
    """Extracts raw text from a PDF file using pdfplumber."""
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"
    return text

def parse_with_llm(raw_text: str) -> str:
    """Uses Google Gemini (Free Tier) to parse messy raw text into structured JSON."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY is not set in .env file.")
        
    client = genai.Client(api_key=api_key)
    
    prompt = f"""
    You are an expert data extraction assistant. I will provide raw text extracted from a financial PDF (invoice).
    Your job is to extract the relevant fields and format them as a JSON object matching the requested schema.
    If a value is missing, infer it from context or use 0 for numbers and "Unknown" for strings.
    
    RAW TEXT:
    {raw_text}
    """
    
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
        config=genai.types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=InvoiceData,
            temperature=0.0
        ),
    )
    
    return response.text

def process_document(pdf_path: str):
    print(f"[*] Processing {pdf_path}...")
    try:
        raw_text = extract_text_from_pdf(pdf_path)
    except Exception as e:
        print(f"[!] Failed to read PDF: {e}")
        return
        
    if not raw_text.strip():
        print("[!] No text found in PDF. It might be a scanned image.")
        return
        
    print("[*] Text extracted successfully. Sending to LLM for structuring...")
    try:
        structured_data = parse_with_llm(raw_text)
        print("\n[+] Extraction Complete! Structured JSON output:")
        print(structured_data)
        
        # Save to file
        output_file = pdf_path.replace('.pdf', '_extracted.json')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(structured_data)
        print(f"\n[*] Saved structured data to: {output_file}")
        
    except Exception as e:
        print(f"[!] Error during LLM parsing: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python extractor.py <path_to_pdf>")
    else:
        process_document(sys.argv[1])
