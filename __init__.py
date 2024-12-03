from cryptography.fernet import Fernet
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

# Génération de la clé pour Fernet
key = Fernet.generate_key()
f = Fernet(key)

# Route pour l'encryptage
@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    valeur_bytes = valeur.encode()  # Conversion str -> bytes
    token = f.encrypt(valeur_bytes)  # Encrypt la valeur
    return f"Valeur encryptée : {token.decode()}"  # Retourne le token en str

# Route pour le décryptage
@app.route('/decrypt/<string:valeur>')
def decryptage(valeur):
    try:
        valeur_bytes = valeur.encode()  # Conversion str -> bytes
        decrypted = f.decrypt(valeur_bytes)  # Décryptage de la valeur
        return f"Valeur décryptée : {decrypted.decode()}"  # Retourne la valeur originale en str
    except Exception as e:
        return f"Erreur lors du décryptage : {e}"

if __name__ == "__main__":
    app.run(debug=True)
