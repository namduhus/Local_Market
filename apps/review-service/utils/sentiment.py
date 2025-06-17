from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

MODEL_NAME = "nlp04/korean_sentiment_analysis_kcelectra"

# 모델 한 번만 로딩
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

id2label = {0: "부정", 1: "중립", 2: "긍정"}
# 긍정 키워드 및 도메인 키워드
positive_keywords = ["좋아요", "추천", "만족", "친절", "힐링", "감사", "재밌었어요", "즐거웠어요", "감동"]
domain_keywords = ["귀농", "귀촌", "로컬", "마을", "농촌", "정착", "체험", "전통"]

# 긍정 키워드 보정
def correct_sentiment(text: str, prediction: str) -> str:
    if prediction == "부정":
        for word in positive_keywords:
            if word in text:
                return "긍정"
    return prediction

# 도메인 키워드 체크
def is_local_context(text: str) -> bool:
    return any(word in text for word in domain_keywords)

# 평점 기반 감정
def rating_based_sentiment(rating: int) -> str:
    if rating <= 2:
        return "부정"
    elif rating == 3:
        return "중립"
    else:
        return "긍정"

# 최종 감정 분석 (텍스트 + 평점 기반)
def analyze_sentiment_with_rating(text: str, rating: int) -> str:
    # 모델 기반 감정 예측
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    predicted_class = torch.argmax(logits, dim=1).item()
    model_result = id2label.get(predicted_class, "중립")  # fallback

    # 키워드 보정
    corrected = correct_sentiment(text, model_result)

    # 도메인 맥락 보정 (선택 사항)
    if corrected == "부정" and is_local_context(text):
        corrected = "중립"

    # 평점 기반 판단
    rating_result = rating_based_sentiment(rating)

    # 종합 판단
    if corrected == rating_result:
        return corrected
    elif rating == 3:
        return corrected  # 중립 평점이면 텍스트 우선
    else:
        return rating_result  # 평점이 강한 경우 평점 우선