from fpdf import FPDF

def create_dummy_invoice():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", size=12)
    
    # Header
    pdf.set_font("helvetica", style="B", size=16)
    pdf.cell(200, 10, text="INVOICE", new_x="LMARGIN", new_y="NEXT", align='C')
    pdf.set_font("helvetica", size=12)
    pdf.cell(200, 10, text="Invoice Number: INV-2026-9912", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(200, 10, text="Date: May 25, 2026", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(200, 10, text="Vendor: TechCorp Solutions LLC", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(200, 10, text="", new_x="LMARGIN", new_y="NEXT")
    
    # Line items header
    pdf.set_font("helvetica", style="B", size=12)
    pdf.cell(80, 10, text="Description")
    pdf.cell(30, 10, text="Quantity")
    pdf.cell(40, 10, text="Unit Price")
    pdf.cell(40, 10, text="Total", new_x="LMARGIN", new_y="NEXT")
    
    pdf.set_font("helvetica", size=12)
    # Item 1
    pdf.cell(80, 10, text="Server Maintenance")
    pdf.cell(30, 10, text="2.0")
    pdf.cell(40, 10, text="$150.00")
    pdf.cell(40, 10, text="$300.00", new_x="LMARGIN", new_y="NEXT")
    
    # Item 2
    pdf.cell(80, 10, text="AI API Credits")
    pdf.cell(30, 10, text="1.0")
    pdf.cell(40, 10, text="$50.00")
    pdf.cell(40, 10, text="$50.00", new_x="LMARGIN", new_y="NEXT")
    
    pdf.cell(200, 10, text="", new_x="LMARGIN", new_y="NEXT")
    
    # Total
    pdf.set_font("helvetica", style="B", size=12)
    pdf.cell(150, 10, text="Total Amount:", align="R")
    pdf.cell(40, 10, text="$350.00", new_x="LMARGIN", new_y="NEXT")
    
    pdf.output("sample_invoice.pdf")
    print("Created sample_invoice.pdf")

if __name__ == "__main__":
    create_dummy_invoice()
