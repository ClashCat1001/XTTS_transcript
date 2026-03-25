from TTS.api import TTS
import soundfile as sf

# 加载模型
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")

# 测试文本
text = "apple.apple.apple......banana.banana.banana......cat.cat.cat"

# 生成音频
wav = tts.tts(text=text, speaker=None, language="en")

# 保存
sf.write("test.wav", wav, tts.synthesizer.output_sample_rate)

print("音频生成成功：test.wav")