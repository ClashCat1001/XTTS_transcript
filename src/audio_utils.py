# src/audio_utils.py
import os
import soundfile as sf
from TTS.api import TTS

XTTS_MODEL = "tts_models/multilingual/multi-dataset/xtts_v2"
SAMPLE_RATE = 24000
_tts = None

def get_tts():
    global _tts
    if _tts is None:
        print("🔊 正在加载 XTTS-v2 模型...")
        _tts = TTS(XTTS_MODEL)
    return _tts

def pages_to_audio_xtts(
    pages_words,
    pdf_name,
    speaker_path="speaker.wav",
    repeat=3,
    short_pause_sec=0.3,
    long_pause_sec=1.5,
    language="en"
):
    tts = get_tts()
    output_dir = os.path.join("output", pdf_name)
    os.makedirs(output_dir, exist_ok=True)

    if not os.path.exists(speaker_path):
        raise FileNotFoundError(f"❌ speaker.wav 不存在: {speaker_path}")
    print(f"🎤 使用 speaker: {speaker_path}")

    for i, words in enumerate(pages_words):
        print(f"📄 正在处理第 {i+1} 页...")
        audio_segments = []

        for word in words:
            for _ in range(repeat):
                wav = tts.tts(text=word, speaker_wav=speaker_path, language=language)
                audio_segments.extend(wav)
            audio_segments.extend([0] * int(SAMPLE_RATE * short_pause_sec))
        audio_segments.extend([0] * int(SAMPLE_RATE * long_pause_sec))

        output_path = os.path.join(output_dir, f"p{i+1}.wav")
        sf.write(output_path, audio_segments, SAMPLE_RATE)
        print(f"✅ 已保存: {output_path}")