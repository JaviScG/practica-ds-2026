from flask import Flask, request, jsonify
import re

app = Flask(__name__)

class TextAnalyzer:
    """Lógica de negocio para el Cuadrante Q1"""
    
    @staticmethod
    def count_words(text):
        if not text or not isinstance(text, str):
            return 0
        return len(text.strip().split())

    @staticmethod
    def is_palindrome(text):
        if not text or not isinstance(text, str):
            return False
        clean_text = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
        return clean_text == clean_text[::-1] and len(clean_text) > 0

# --- Rutas de la API (Cuadrante Q2 / API First) ---

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "No text provided"}), 400
        
    text = data.get('text', "")
    analyzer = TextAnalyzer()
    
    return jsonify({
        "word_count": analyzer.count_words(text),
        "is_palindrome": analyzer.is_palindrome(text)
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)