# POS Tagging dan Dependency Parsing: Menandai bagian dari ucapan dan menganalisis hubungan gramatikal.
import spacy

# Memuat model bahasa Inggris
nlp = spacy.load('en_core_web_sm')

# Teks untuk analisis
text = "The cat sat on the mat."

# Memproses teks
doc = nlp(text)

# POS Tagging
pos_tags = [(token.text, token.pos_) for token in doc]
print("POS Tags:", pos_tags)

# Dependency Parsing
dependencies = [(token.text, token.dep_, token.head.text) for token in doc]
print("Dependencies:", dependencies)
