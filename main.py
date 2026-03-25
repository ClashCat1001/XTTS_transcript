import os
from src.pdf_utils import extract_pdf_pages
from src.audio_utils import pages_to_audio_xtts

PDF_DIR = "data"
OUTPUT_DIR = "output"


def get_user_input():
    try:
        repeat = int(input("🔁 每个单词重复次数 (默认3): ") or 3)
        short_pause = float(input("⏱️ 短间隔秒 (默认0.3): ") or 0.3)
        long_pause = float(input("⏱️ 长间隔秒 (默认1.5): ") or 1.5)
    except ValueError:
        print("⚠️ 输入无效，使用默认值")
        return 3, 0.3, 1.5

    return repeat, short_pause, long_pause


if __name__ == "__main__":
    repeat, short_pause, long_pause = get_user_input()

    for pdf_file in os.listdir(PDF_DIR):
        if pdf_file.lower().endswith(".pdf"):
            pdf_path = os.path.join(PDF_DIR, pdf_file)
            pdf_name = os.path.splitext(pdf_file)[0]

            pages = extract_pdf_pages(pdf_path)

            pages_to_audio_xtts(
                pages,
                pdf_name=pdf_name,
                output_dir=OUTPUT_DIR,
                repeat=repeat,
                short_pause_sec=short_pause,
                long_pause_sec=long_pause,
                language="en"
            )