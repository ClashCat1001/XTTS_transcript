from src.tts_engine import TTSEngine

tts = TTSEngine()

audio = tts.generate("hello world")

print(audio.shape)