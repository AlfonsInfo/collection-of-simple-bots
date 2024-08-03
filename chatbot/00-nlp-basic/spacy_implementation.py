import spacy

# Memuat model bahasa Inggris
nlp = spacy.load('en_core_web_sm')

# Teks untuk preprocessing
text = "The quick brown fox jumps over the lazy dog."

# Memproses teks
doc = nlp(text)

# Tokenisasi
tokens = [token.text for token in doc]
print("Tokens:", tokens)

# Lematisasi
lemmas = [token.lemma_ for token in doc]
print("Lemmas:", lemmas)
