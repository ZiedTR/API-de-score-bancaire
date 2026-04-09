from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/score', methods=['GET'])
def score_client():
    age = int(request.args.get('age', 30))
    revenus = int(request.args.get('revenus', 1500))
    incidents = int(request.args.get('incidents', 0))
    
    score = 100
    if age < 25: score -= 20
    if revenus < 1000: score -= 30
    elif revenus < 2000: score -= 10
    if incidents > 0: score -= (incidents * 15)
    
    if score >= 70:
        risque = "FAIBLE"
    elif score >= 40:
        risque = "MOYEN"
    else:
        risque = "ÉLEVÉ"
    
    return jsonify({
        "score": max(score, 0),
        "risque": risque,
        "recommandation": "Accord" if score >= 70 else "Refus"
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
