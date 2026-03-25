import os
from src.pdf_utils import extract_pdf_pages
from src.audio_utils import pages_to_audio_ssml

# -----------------------------
# 配置参数
# -----------------------------
DATA_DIR = "data"
OUTPUT_DIR = "output"
REPEAT = 3
SHORT_PAUSE_SEC = 0.3
LONG_PAUSE_SEC = 1.5

os.makedirs(OUTPUT_DIR, exist_ok=True)

# -----------------------------
# 批量处理 PDF
# -----------------------------
for file_name in os.listdir(DATA_DIR):
    if file_name.lower().endswith(".pdf"):
        pdf_path = os.path.join(DATA_DIR, file_name)
        pdf_name = os.path.splitext(file_name)[0]

        print(f"📄 Processing PDF: {file_name}")
        pages = extract_pdf_pages(pdf_path)
        pages_to_audio_ssml(
            pages,
            pdf_name,
            output_dir=OUTPUT_DIR,
            repeat=REPEAT,
            short_pause_sec=SHORT_PAUSE_SEC,
            long_pause_sec=LONG_PAUSE_SEC
        )

print("✅ All PDFs processed.")