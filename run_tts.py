from TTS.api import TTS

tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC")

tts.tts_to_file(
    text="The word is phenomenon.",
    file_path="test.wav"
)

print("DONE")
