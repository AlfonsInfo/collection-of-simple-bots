from transformers import pipeline

# Membuat pipeline untuk analisis sentimen
sentiment_pipeline = pipeline('sentiment-analysis')

# Fungsi untuk menganalisis sentimen
def analyze_sentiment(text):
    result = sentiment_pipeline(text)
    return result

# Contoh penggunaan
text = "I love using Python for data analysis!"
sentiment = analyze_sentiment(text)
print(sentiment)
