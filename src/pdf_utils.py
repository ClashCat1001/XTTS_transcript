import pdfplumber

def extract_pdf_pages(pdf_path):
    """
    提取 PDF 每页表格首列单词
    返回 [[page1_words], [page2_words], ...]
    """
    pages_words = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            words = []
            tables = page.extract_tables()
            if tables:
                for row in tables[0]:  # 只取第一个表格
                    if row and row[0]:
                        words.append(row[0])
            pages_words.append(words)
    return pages_words