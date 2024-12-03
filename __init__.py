from cryptography.fernet import Fernet
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Fonction pour charger ou générer une clé persistante
def load_or_generate_key():
    try:
        with open("secret.key", "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
        return key

# Charger la clé persistante
key = load_or_generate_key()
f = Fernet(key)

@app.route('/')
def hello_world():
    return render_template('hello.html')

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
