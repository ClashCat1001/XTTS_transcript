import pdfplumber

def extract_pdf_pages(pdf_path: str):
    """
    提取 PDF 每页表格首列单词
    :return: [[page1_words], [page2_words], ...]
    """
    pages = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            words = []
            tables = page.extract_tables()
            for table in tables:
                for row in table:
                    if row and row[0]:
                        words.append(str(row[0]))
            pages.append(words)
    return pages