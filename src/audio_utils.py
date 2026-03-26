import os
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
    repeat=3,
    short_pause_sec=0.3,
    long_pause_sec=1.5,
    language="en"
):
    tts = get_tts()

    # 输出目录
    output_dir = os.path.join("output", pdf_name)
    os.makedirs(output_dir, exist_ok=True)

    speaker_path = os.path.join(os.getcwd(), "speaker.wav")

    if not os.path.exists(speaker_path):
        raise FileNotFoundError("❌ speaker.wav 不存在，请先生成")

    print(f"🎤 使用 speaker: {speaker_path}")

    for i, page in enumerate(pages):
        print(f"📄 正在处理第 {i+1} 页...")

        words = page.split()
        audio_segments = []

        for word in words:
            for _ in range(repeat):
                wav = tts.tts(
                    text=word,
                    speaker_wav=speaker_path,
                    language=language
                )
                audio_segments.extend(wav)

                # 短停顿
                silence = [0] * int(24000 * short_pause_sec)
                audio_segments.extend(silence)

        # 长停顿（页结束）
        silence = [0] * int(24000 * long_pause_sec)
        audio_segments.extend(silence)

        output_path = os.path.join(output_dir, f"p{i+1}.wav")

        sf.write(output_path, audio_segments, 24000)

        print(f"✅ 已保存: {output_path}")