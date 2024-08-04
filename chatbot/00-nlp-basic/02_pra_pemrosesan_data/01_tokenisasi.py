import spacy

# Memuat model bahasa Inggris
nlp = spacy.load('en_core_web_sm')

# Teks untuk tokenisasi
text = "Hello, how are you doing today?"

# Memproses teks
doc = nlp(text)

# Tokenisasi
tokens = [token.text for token in doc]
print("Tokens:", tokens)
