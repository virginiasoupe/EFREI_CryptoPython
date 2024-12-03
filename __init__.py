from cryptography.fernet import Fernet
from flask import Flask, render_template

app = Flask(__name__)

# Générer une clé et créer une instance de Fernet
key = Fernet.generate_key()
f = Fernet(key)

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    valeur_bytes = valeur.encode()  # Conversion str -> bytes
    token = f.encrypt(valeur_bytes)  # Encrypt la valeur
    return f"Valeur encryptée : {token.decode()}"  # Retourne le token en str

@app.route('/decrypt/<string:token>')
def decryptage(token):
    token_bytes = token.encode()  # Conversion str -> bytes
    valeur_bytes = f.decrypt(token_bytes)  # Decrypt le token
    return f"Valeur décryptée : {valeur_bytes.decode()}"  # Retourne la valeur en str

if __name__ == "__main__":
    app.run(debug=True)

