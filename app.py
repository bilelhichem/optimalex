from flask import Flask, request, jsonify
from services.prompt_service import get_prompt

app = Flask(__name__)

@app.route('/match_prompt', methods=['POST'])
def match_prompt():
    try:
        data = request.get_json()

      
        if not data:
            return jsonify({"error": "Missing Data"}), 400.   # Vérifier si le JSON est bien formé

        
        required_fields = ["situation", "level", "file_type", "data"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": "Missing Data"}), 400 # Vérifier la présence des champs obligatoires

        # Obtenir le prompt correspondant
        prompt = get_prompt(
            data["situation"],
            data["level"],
            data["file_type"]
        )

        if prompt:
            return jsonify({"prompt": prompt}), 200
        else:
            return jsonify({"error": "Invalid Prompt"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
