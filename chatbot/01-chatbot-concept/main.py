from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    
    # Logika sederhana untuk merespons pesan
    if not user_message:
        return jsonify({'response': 'Pesan tidak ditemukan.'})

    user_message = user_message.lower()

    if 'hello' in user_message:
        response = 'Halo! Bagaimana saya bisa membantu Anda?'
    elif 'how are you' in user_message:
        response = 'Saya baik, terima kasih! Bagaimana dengan Anda?'
    elif 'bye' in user_message:
        response = 'Selamat tinggal! Semoga hari Anda menyenangkan!'
    else:
        response = 'Maaf, saya tidak mengerti pesan Anda. Coba pesan lain.'
    
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
