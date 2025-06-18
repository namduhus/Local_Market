from keybert import KeyBERT

kw_model = KeyBERT(model='distiluse-base-multilingual-cased-v1')

KOREAN_STOPWORDS = [
    "은", "는", "이", "가", "을", "를", "에", "의", "도", "다", "고", "하", "그", "수", "들",
    "으로", "와", "과", "해서", "이다", "있는", "되", "것", "때", "더", "이번", "정말", "너무"
]

def clean_keywords(keywords: list[str]) -> list[str]:
    seen = set()
    cleaned = []
    for kw in keywords:
        kw = kw.strip()

        # 조사 제거 (뒤에서 하나 또는 두 글자 제거)
        while len(kw) > 2 and kw[-1] in KOREAN_STOPWORDS:
            kw = kw[:-1]

        # 중복 제거 (이미 포함된 키워드의 일부인 경우 스킵)
        if kw not in seen and all(kw not in existing for existing in cleaned):
            cleaned.append(kw)
            seen.add(kw)

    return cleaned

def extract_keywords(text: str, top_n: int = 5) -> list[str]:
    raw_keywords = kw_model.extract_keywords(
        text,
        keyphrase_ngram_range=(1, 2),
        stop_words=KOREAN_STOPWORDS,
        top_n=top_n
    )
    top_phrases = [kw[0] for kw in raw_keywords]
    return clean_keywords(top_phrases)
