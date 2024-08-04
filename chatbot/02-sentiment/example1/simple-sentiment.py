from transformers import pipeline

# Membuat pipeline untuk analisis sentimen
sentiment_pipeline = pipeline('sentiment-analysis' )
# sentiment_pipeline = pipeline('sentiment-analysis' , model=)

# Fungsi untuk menganalisis sentimen
# saat di deploy, fungsi ini akan dipanggil saat startup aplikasi
def analyze_sentiment(text):
    result = sentiment_pipeline(text)
    return result

# Contoh penggunaan
text = "I love this movie!"
sentiment = analyze_sentiment(text)
print(sentiment)
