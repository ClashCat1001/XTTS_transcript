import os
import soundfile as sf

from src.pdf_parser import extract_first_column_by_page
from src.text_processor import split_text
from src.tts_engine import TTSEngine
from src.audio_utils import concat_audio


def main():
    pdf_path = "data/input.pdf"
    output_dir = "output"

    os.makedirs(output_dir, exist_ok=True)

    # 1. 解析PDF
    pages_data = extract_first_column_by_page(pdf_path)

    # 2. 初始化TTS
    tts = TTSEngine()

    # 3. 逐页处理
    for i, words in enumerate(pages_data):
        if not words:
            continue

        text = " ".join(words)
        chunks = split_text(text)

        audio_chunks = []

        for chunk in chunks:
            audio = tts.generate(chunk)
            audio_chunks.append(audio)

        final_audio = concat_audio(audio_chunks)

        sf.write(f"{output_dir}/page_{i+1}.wav", final_audio, samplerate=24000)

        print(f"Page {i+1} done")


if __name__ == "__main__":
    main()