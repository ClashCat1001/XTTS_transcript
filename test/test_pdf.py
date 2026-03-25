from src.pdf_parser import extract_first_column_by_page

pages = extract_first_column_by_page("data/input.pdf")

print(pages[:2])