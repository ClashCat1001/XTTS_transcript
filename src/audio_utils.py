from transformers import pipeline
import torch
import os

# XTTS-v2 英音开源模型
XTTS_MODEL = "espnet/kan-bayashi_ljspeech_vits"  # 可换成你的本地 XTTS-v2 模型

device = 0 if torch.cuda.is_available() else -1
tts = pipeline("text-to-speech", model=XTTS_MODEL, device=device)

def pages_to_audio_ssml(pages, pdf_name, output_dir, repeat=3, short_pause_sec=0.3, long_pause_sec=1.5):
    """
    pages: [[page1_words], [page2_words], ...]
    repeat: 每个单词重复次数
    short_pause_sec: 单词内部重复的短间隔
    long_pause_sec: 单词间长间隔
    """
    for i, page_words in enumerate(pages, 1):
        ssml_segments = []
        for word in page_words:
            repeated = f'<break time="{short_pause_sec}s"/>'.join([word]*repeat)
            ssml_segments.append(repeated)
        ssml_text = f'<break time="{long_pause_sec}s"/>'.join(ssml_segments)

        output_path = os.path.join(output_dir, f"{pdf_name}_page_{i}.wav")
        tts(ssml_text, output_path=output_path)