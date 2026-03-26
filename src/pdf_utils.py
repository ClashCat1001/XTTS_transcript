import pdfplumber
import pandas as pd

def extract_pdf_pages(pdf_path):
    """提取 PDF 每页文本"""
    pages = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                pages.append(text)
    return pages

def extract_table_first_column(pdf_path):
    """提取 PDF 所有表格的第一列（通常为单词/词组）"""
    first_col_list = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()
            for table in tables:
                for row in table:
                    if row and row[0]:
                        first_col_list.append(row[0])
    return first_col_list