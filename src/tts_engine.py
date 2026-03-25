from transformers import AutoModelForTextToSpeech, AutoTokenizer
import torch

class TTSEngine:
    def __init__(self):
        model_name = "coqui/XTTS-v2"

        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForTextToSpeech.from_pretrained(model_name)

        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = self.model.to(self.device)

    def generate(self, text):
        inputs = self.tokenizer(text, return_tensors="pt").to(self.device)

        with torch.no_grad():
            audio = self.model.generate(**inputs)

        return audio.cpu().numpy()