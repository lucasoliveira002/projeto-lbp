# Em controllers/ia_controller.py
from flask import Blueprint, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

ia_bp = Blueprint('ia', __name__)

@ia_bp.route('/ia_response', methods=['POST'])
def ia_response():
   data = request.get_json()
   question = data.get('question')

   if question:
       try:
           model = genai.GenerativeModel('gemini-pro')
           response = model.generate_content(question)
           answer = response.text

       except Exception as e:
             answer = f"Desculpe, ocorreu um erro ao processar sua pergunta. Tente novamente mais tarde. {e}"
   else:
       answer = "Nenhuma pergunta foi feita!"
   return jsonify({'response': answer})