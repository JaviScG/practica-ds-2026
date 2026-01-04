import pytest
from app import TextAnalyzer, app

# Q1: Tests Unitarios (Frecuentes y automatizados)
def test_word_count():
    analyzer = TextAnalyzer()
    assert analyzer.count_words("Hola mundo") == 2
    assert analyzer.count_words("") == 0

# Q2: Test de Integración (Interacción de módulos)
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_api_analyze(client):
    # Simulación de un caso de uso de negocio 
    response = client.post('/analyze', json={"text": "radar"})
    assert response.status_code == 200
    assert response.get_json()["is_palindrome"] is True

def test_count_vowels():
    analyzer = TextAnalyzer()
    # Caso 1: Texto con vocales variadas
    assert analyzer.count_vowels("Murcielago") == 5
    # Caso 2: Texto sin vocales
    assert analyzer.count_vowels("Ply") == 0
    # Caso 3: Mayúsculas y minúsculas
    assert analyzer.count_vowels("AeIoU") == 5