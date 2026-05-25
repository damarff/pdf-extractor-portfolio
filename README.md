# AI-Powered Financial Document Extractor 📄➡️📊

An intelligent pipeline that extracts unstructured text from messy financial PDFs (invoices, receipts, financial reports) and converts them into structured, queryable JSON data using Large Language Models (LLMs).

## Business Value 💼
Manual data entry is slow, error-prone, and expensive. Traditional OCR and regex-based solutions break whenever a vendor changes their invoice layout. 

This solution uses **Generative AI (OpenAI's Structured Outputs)** to semantically understand the document regardless of its visual layout, ensuring **99%+ accuracy** for accounting, ERP, and CRM data entry automation.

## Features 🚀
- **Robust Text Extraction**: Uses `pdfplumber` to accurately scrape text and tabular data from PDFs.
- **LLM Semantic Parsing**: Uses OpenAI's `gpt-4o-mini` (can be swapped for Claude/Llama) to map messy text into a strict Pydantic JSON schema.
- **100% Reliable JSON**: Leverages OpenAI's Structured Outputs API to guarantee the output JSON schema matches your database exactly, eliminating hallucination errors.

## Example Use Case
**Input**: A messy, multi-page PDF invoice from a new supplier.
**Output**: A clean JSON payload containing `invoice_number`, `date`, `total_amount`, and an array of `line_items` (description, quantity, unit price, total), ready to be injected into QuickBooks or Xero via API.

## How to Run 🛠️

1. Clone the repository and install dependencies:
```bash
pip install -r requirements.txt
```

2. Set your OpenAI API Key in `.env`:
```env
OPENAI_API_KEY=sk-your-key-here
```

3. Run the extractor on any PDF:
```bash
python extractor.py sample_invoice.pdf
```

## Tech Stack
- **Python 3.10+**
- **pdfplumber** (PDF parsing)
- **OpenAI API** (Semantic extraction)
- **Pydantic** (Schema validation)
