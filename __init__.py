from cryptography.fernet import Fernet
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Clé de chiffrement/déchiffrement
key = Fernet.generate_key()
f = Fernet(key)

@app.route('/')
def hello_world():
    return render_template('hello.html')

# Route pour chiffrer une valeur
@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    valeur_bytes = valeur.encode()  # Conversion str -> bytes
    token = f.encrypt(valeur_bytes)  # Chiffrement de la valeur
    return f"Valeur encryptée : {token.decode()}"  # Retourne le token en str

# Nouvelle route pour déchiffrer une valeur via URL
@app.route('/decrypt/<string:encrypted_val>')
def decryptage(encrypted_val):
    try:
        # Conversion de la valeur chiffrée en bytes
        encrypted_bytes = encrypted_val.encode()
        # Déchiffrement de la valeur
        decrypted_text = f.decrypt(encrypted_bytes).decode()
        return f"Valeur décryptée : {decrypted_text}"
    except Exception as e:
        # Gestion des erreurs, par ex. si le texte est invalide
        return f"Erreur : {str(e)}", 400

if __name__ == "__main__":
    app.run(debug=True)
