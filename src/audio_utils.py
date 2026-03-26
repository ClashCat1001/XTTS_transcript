from TTS.api import TTS
import os
import soundfile as sf
import numpy as np

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

    pdf_folder = os.path.join(output_dir, pdf_name)
    os.makedirs(pdf_folder, exist_ok=True)

    sample_rate = 22050
    short_pause = np.zeros(int(sample_rate * short_pause_sec))
    long_pause = np.zeros(int(sample_rate * long_pause_sec))

    for i, page in enumerate(pages, start=1):
        print(f"📄 正在处理第 {i} 页...")

        words = page.split()
        audio_segments = []

        for word in words:
            for _ in range(repeat):
                wav = tts.tts(
                    text=word,
                    speaker_wav="speaker.wav",   # ✅ 使用你的 BBC 声音
                    language=language
                )
                audio_segments.append(np.array(wav))
                audio_segments.append(short_pause)

            audio_segments.append(long_pause)

        final_audio = np.concatenate(audio_segments)

        output_path = os.path.join(pdf_folder, f"p{i}.wav")
        sf.write(output_path, final_audio, sample_rate)

        print(f"✅ 已生成: {output_path}")