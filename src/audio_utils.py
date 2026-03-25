import os
from transformers import pipeline
import torch

# 英音模型
ENGLISH_SPEAKER_MODEL = "microsoft/speech-t5_tts"

device = 0 if torch.cuda.is_available() else -1

tts = pipeline(
    "text-to-speech",
    model=ENGLISH_SPEAKER_MODEL,
    device=device
)

def text_to_speech_ssml(ssml_text: str, output_path: str):
    """使用 SSML 生成 WAV 文件"""
    tts(ssml_text, output_path=output_path)

def repeat_words_with_ssml(words: list,
                           repeat: int = 3,
                           short_pause_sec: float = 0.3,
                           long_pause_sec: float = 1.5):
    """
    拼接单词成 SSML 文本：单词重复 + 短停顿 + 长停顿
    """
    repeated_words = []
    for word in words:
        repeated = f'<break time="{short_pause_sec}s"/>'.join([word] * repeat)
        repeated_words.append(repeated)

    ssml_text = f'<break time="{long_pause_sec}s"/>'.join(repeated_words)
    return f"<speak>{ssml_text}</speak>"

def pages_to_audio_ssml(pages: list,
                        pdf_name: str,
                        output_dir: str = "output",
                        repeat: int = 3,
                        short_pause_sec: float = 0.3,
                        long_pause_sec: float = 1.5):
    """
    批量生成每页音频
    """
    os.makedirs(output_dir, exist_ok=True)

    for i, page_words in enumerate(pages, start=1):
        ssml_text = repeat_words_with_ssml(
            page_words,
            repeat=repeat,
            short_pause_sec=short_pause_sec,
            long_pause_sec=long_pause_sec
        )
        output_path = os.path.join(output_dir, f"{pdf_name}_page_{i}.wav")
        text_to_speech_ssml(ssml_text, output_path)
        print(f"✅ Page {i} audio saved: {output_path}")