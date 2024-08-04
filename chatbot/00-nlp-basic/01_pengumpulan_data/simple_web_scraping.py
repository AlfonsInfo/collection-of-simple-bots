import requests
from bs4 import BeautifulSoup

# URL halaman yang akan di-scrape
url = 'https://aws.amazon.com/id/what-is/nlp/'

# Mengambil konten halaman
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Menemukan dan mencetak semua elemen dengan tag <p>
text = ''
for p in soup.find_all('p'):
    text += p.get_text() + '\n'
    print(p.get_text())
    # masukin ke text file

with open('hasil.txt', 'w') as file:
    file.write(text)