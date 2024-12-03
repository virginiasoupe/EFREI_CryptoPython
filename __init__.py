from cryptography.fernet import Fernet
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Génération ou récupération de la clé
key_file = "secret.key"

def load_or_generate_key():
    try:
        with open(key_file, "rb") as file:
            return file.read()
    except FileNotFoundError:
        key = Fernet.generate_key()
        with open(key_file, "wb") as file:
            file.write(key)
        return key

# Charger la clé persistante
key = load_or_generate_key()
cipher = Fernet(key)

@app.route('/')
def hello_world():
    return render_template('hello.html')

# Route pour chiffrer une valeur
@app.route('/encrypt/<string:valeur>')
def encrypt(valeur):
    try:
        encrypted_value = cipher.encrypt(valeur.encode())  # Chiffrement
        return f"Valeur chiffrée : {encrypted_value.decode()}"  # Convertir en str
    except Exception as e:
        return f"Erreur lors du chiffrement : {e}"

# Route pour déchiffrer une valeur
@app.route('/decrypt/<string:valeur>')
def decrypt(valeur):
    try:
        decrypted_value = cipher.decrypt(valeur.encode())  # Déchiffrement
        return f"Valeur déchiffrée : {decrypted_value.decode()}"  # Convertir en str
    except Exception as e:
        return f"Erreur lors du déchiffrement : {e}"

if __name__ == "__main__":
    app.run(debug=True)
