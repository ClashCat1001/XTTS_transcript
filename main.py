import os
from src.pdf_utils import extract_pdf_pages
from src.audio_utils import pages_to_audio_xtts
from tools.extract_speaker import extract_speaker


def safe_input(prompt, default):
    try:
        value = input(prompt).strip()
        return float(value) if value else default
    except ValueError:
        print("⚠️ 输入无效，使用默认值")
        return default


def main():
    pdf_path = input("📄 输入 PDF 路径: ").strip()
    if not os.path.exists(pdf_path):
        print("❌ PDF 文件不存在")
        return

    repeat = int(safe_input("🔁 每个单词重复次数 (默认3): ", 3))
    short_pause = safe_input("⏱️ 短间隔秒 (默认0.3): ", 0.3)
    long_pause = safe_input("⏱️ 长间隔秒 (默认1.5): ", 1.5)

    # 🔥 自动生成 speaker.wav
    extract_speaker(
        input_path="sample.wav",
        output_path="speaker.wav",
        duration_sec=6
    )

    pages = extract_pdf_pages(pdf_path)

    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]

    pages_to_audio_xtts(
        pages,
        pdf_name,
        repeat=repeat,
        short_pause_sec=short_pause,
        long_pause_sec=long_pause,
    )


if __name__ == "__main__":
    main()