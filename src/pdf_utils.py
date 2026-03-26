# src/pdf_utils.py
import pdfplumber

def extract_pdf_pages(pdf_path):
    """
    提取 PDF 页面文本或表格第一列
    返回列表，每页为一个单词/词组列表
    """
    pages_words = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            # 尝试提取表格
            table = page.extract_table()
            if table:
                first_col = [row[0] for row in table if row[0]]
                pages_words.append(first_col)
            else:
                text = page.extract_text()
                if text:
                    pages_words.append(text.split())
    return pages_words