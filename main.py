import os
import json
from src.pdf_utils import extract_pdf_pages, extract_table_first_column

def safe_input(prompt, default):
    value = input(prompt)
    try:
        return float(value)
    except ValueError:
        print("⚠️ 输入无效，使用默认值")
        return default

if __name__ == "__main__":
    pdf_path = input("📄 输入 PDF 文件名（例如 example.pdf）: ").strip()
    if not os.path.exists(pdf_path):
        raise FileNotFoundError("❌ PDF 文件不存在")

    repeat = int(safe_input("🔁 每个单词重复次数 (默认3): ", 3))
    short_pause = safe_input("⏱️ 短间隔秒 (默认0.3): ", 0.3)
    long_pause = safe_input("⏱️ 长间隔秒 (默认1.5): ", 1.5)

    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]

    print("📖 正在解析 PDF...")
    # 提取分页文本或表格第一列
    pages = extract_pdf_pages(pdf_path)
    table_words = extract_table_first_column(pdf_path)
    if table_words:
        print(f"📊 表格第一列提取到 {len(table_words)} 个单词/词组")
        pages.append(" ".join(table_words))  # 可合并到最后一页或另起一页

    # 保存 JSON
    with open(f"{pdf_name}_pages.json", "w", encoding="utf-8") as f:
        json.dump(pages, f, ensure_ascii=False, indent=2)

    params = {
        "repeat": repeat,
        "short_pause": short_pause,
        "long_pause": long_pause,
        "pdf_name": pdf_name
    }
    with open(f"{pdf_name}_params.json", "w", encoding="utf-8") as f:
        json.dump(params, f, ensure_ascii=False, indent=2)

    print(f"✅ PDF 分析完成，生成 {pdf_name}_pages.json 和 {pdf_name}_params.json")
    print("💡 请确保 speaker.wav 在当前目录，并 push 这三个文件到 GitHub 供 Colab 使用")