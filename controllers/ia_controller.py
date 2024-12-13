# Em controllers/ia_controller.py
from flask import Blueprint, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-small"
headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}", "Content-Type": "application/json"}

ia_bp = Blueprint('ia', __name__)

@ia_bp.route('/ia_response', methods=['POST'])
def ia_response():
    data = request.get_json()
    question = data.get('question')

    if question:
        try:
            payload = {"inputs": [question]}
            response = requests.post(API_URL, headers=headers, json=payload)
            response.raise_for_status() # Gera um erro para status codes ruins (4xx ou 5xx)
            answer = response.json()[0]['generated_text']
        except requests.exceptions.RequestException as e:
             answer = f"Desculpe, ocorreu um erro ao processar sua pergunta. Tente novamente mais tarde. Erro de conexão: {e} - Dados: {payload}"
        except KeyError as e:
             answer = f"Desculpe, ocorreu um erro ao processar sua pergunta. Tente novamente mais tarde. Erro ao extrair resposta: {e} - Resposta: {response.json()}"
        except Exception as e:
            answer = f"Desculpe, ocorreu um erro ao processar sua pergunta. Tente novamente mais tarde. {e}"
    else:
        answer = "Nenhuma pergunta foi feita!"

    return jsonify({'response': answer})

