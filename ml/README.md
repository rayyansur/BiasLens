# ML Pipeline

## Model Checkpoints

Checkpoints are **not committed**. To download the base model locally:

```bash
pip install transformers torch
python -c "from transformers import AutoModel; AutoModel.from_pretrained('cardiffnlp/twitter-roberta-base-sentiment')"
```

Fine-tuned checkpoints should be placed in `checkpoints/` (gitignored).

## Scripts

| Script | Purpose |
|---|---|
| `scripts/train.py` | Fine-tune the bias classifier |
| `scripts/evaluate.py` | Evaluate a checkpoint on the test set |
| `scripts/ingest.py` | Pull articles from NewsAPI into the DB |
