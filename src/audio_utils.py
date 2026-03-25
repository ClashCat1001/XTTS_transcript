import os
import numpy as np
import soundfile as sf
from TTS.api import TTS

XTTS_MODEL = "tts_models/multilingual/multi-dataset/xtts_v2"

_tts = None


def get_tts():
    global _tts
    if _tts is None:
        print("🔊 正在加载 XTTS-v2 模型...")
        _tts = TTS(XTTS_MODEL)
    return _tts


def pages_to_audio_xtts(
    pages,
    pdf_name,
    output_dir="output",
    repeat=3,
    short_pause_sec=0.3,
    long_pause_sec=1.5,
    language="en"
):
    tts = get_tts()

    # 清理文件名
    pdf_name = pdf_name.replace(" ", "_")

    pdf_output_dir = os.path.join(output_dir, pdf_name)
    os.makedirs(pdf_output_dir, exist_ok=True)

    sr = tts.synthesizer.output_sample_rate

    short_pause = np.zeros(int(short_pause_sec * sr))
    long_pause = np.zeros(int(long_pause_sec * sr))

    for idx, page in enumerate(pages, start=1):
        if not page:
            continue

        audio_segments = []

        for word in page:
            for r in range(repeat):
                wav = tts.tts(text=word, speaker=None, language=language)
                audio_segments.append(wav)

                # 🔹 短间隔（重复之间）
                if r < repeat - 1:
                    audio_segments.append(short_pause)

            # 🔸 长间隔（单词之间）
            audio_segments.append(long_pause)

        if not audio_segments:
            continue

        full_audio = np.concatenate(audio_segments)

        out_path = os.path.join(pdf_output_dir, f"p{idx}.wav")

        sf.write(out_path, full_audio, sr)
        print(f"✅ 生成: {out_path}")