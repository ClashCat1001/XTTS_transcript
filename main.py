# main.py
import os
from src.pdf_utils import extract_pdf_pages
from src.audio_utils import pages_to_audio_xtts

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
    pages_words = extract_pdf_pages(pdf_path)

    pages_to_audio_xtts(
        pages_words,
        pdf_name,
        repeat=repeat,
        short_pause_sec=short_pause,
        long_pause_sec=long_pause
    )
    print("🎉 全部完成！")