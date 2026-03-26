import librosa
import soundfile as sf
import os

def extract_speaker(
    input_path="sample.wav",
    output_path="speaker.wav",
    duration_sec=6,
    target_sr=22050
):
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"{input_path} 不存在")

    print(f"🎧 加载音频: {input_path}")
    y, sr = librosa.load(input_path, sr=target_sr)

    total_duration = len(y) / sr

    if total_duration < duration_sec:
        print("⚠️ 音频太短，直接使用原音频")
        sf.write(output_path, y, sr)
        return

    # 🎯 从中间截取
    start_time = (total_duration - duration_sec) / 2
    end_time = start_time + duration_sec

    start_sample = int(start_time * sr)
    end_sample = int(end_time * sr)

    y_cut = y[start_sample:end_sample]

    sf.write(output_path, y_cut, sr)

    print(f"✅ 已生成 speaker: {output_path}")
    print(f"⏱️ 时长: {duration_sec}s | 采样率: {sr}")

if __name__ == "__main__":
    extract_speaker()