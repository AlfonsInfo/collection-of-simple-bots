# pembersihan kata-kata

import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Pastikan Anda sudah mengunduh stopwords dan wordnet dengan nltk.download()
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# Teks untuk pembersihan
text = "The quick brown foxes are running and jumping over the lazy dogs!"

# Menghapus tanda baca dan mengubah teks menjadi huruf kecil
text = re.sub(r'[^\w\s]', '', text).lower()

# Tokenisasi
tokens = word_tokenize(text)

# Menghapus stop words dan melakukan lemmatization
filtered_tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
print("Cleaned Tokens:", filtered_tokens)
