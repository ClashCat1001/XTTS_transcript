import pdfplumber

def extract_pdf_pages(pdf_path):
    pages = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables() or []

            words = [
                str(row[0]).strip()
                for table in tables
                for row in table
                if row and row[0]
            ]

            pages.append(words)

    return pages