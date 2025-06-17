from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

MODEL_NAME = "nlp04/korean_sentiment_analysis_kcelectra"

# 모델 한 번만 로딩
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

id2label = {0: "부정", 1: "중립", 2: "긍정"}

def analyze_sentiment(text: str) -> str:
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    predicted = torch.argmax(logits, dim=1).item()
    return id2label[predicted]
