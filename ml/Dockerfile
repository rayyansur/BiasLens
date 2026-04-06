FROM python:3.12-slim

WORKDIR /app

# torch is large — install before copying source so layer is cached
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Pre-download the HuggingFace model weights at build time
RUN python -c "\
from transformers import AutoTokenizer, AutoModelForSequenceClassification; \
AutoTokenizer.from_pretrained('cardiffnlp/twitter-roberta-base-sentiment'); \
AutoModelForSequenceClassification.from_pretrained('cardiffnlp/twitter-roberta-base-sentiment')"

CMD ["uvicorn", "ml.serve:app", "--host", "0.0.0.0", "--port", "8001"]
