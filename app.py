from flask import Flask, render_template, jsonify

app = Flask(__name__)

PROFILE = {
    "name": "RAMZI",
    "handle": "NIGHT CITY NETRUNNER",
    "level": 15,
    "status": "EN LIGNE",
    "class": "ÉTUDIANT • GAMER • CRÉATEUR",
    "bio": "Curieux, ambitieux et toujours prêt à apprendre quelque chose de nouveau.",
    "stats": [
        {"label": "Curiosité", "value": 92},
        {"label": "Créativité", "value": 84},
        {"label": "Détermination", "value": 88},
        {"label": "Stratégie", "value": 90}
    ],
    "interests": ["Manga & anime", "Jeux vidéo", "Technologie", "Histoire & géopolitique", "Sciences"],
    "projects": [
        {"name": "PROJECT: REVENGE", "type": "GAME DEV", "description": "Un jeu narratif mystérieux autour de fragments de mémoire et d'une enquête."},
        {"name": "RAMZI.exe", "type": "WEB DESIGN", "description": "Mon espace personnel : idées, projets et objectifs."},
        {"name": "JAPAN.exe", "type": "FUTURE PLAN", "description": "Un futur voyage à préparer : Tokyo, Kyoto, Osaka et bien plus."}
    ]
}

@app.route("/")
def index():
    return render_template("index.html", profile=PROFILE)

@app.route("/api/status")
def status():
    return jsonify({"status": "ONLINE", "system": "RAMZI.exe", "level": PROFILE["level"]})

if __name__ == "__main__":
    app.run(debug=True)
