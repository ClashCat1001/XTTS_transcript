import pdfplumber

def extract_first_column_by_page(pdf_path):
    pages_data = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            words = []

            tables = page.extract_tables()

            for table in tables:
                for row in table:
                    if row and row[0]:
                        words.append(row[0].strip())

            pages_data.append(words)

    return pages_data