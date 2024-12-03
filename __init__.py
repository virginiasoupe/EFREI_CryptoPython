from cryptography.fernet import Fernet
from flask import Flask, render_template

app = Flask(__name__)

# Générer une clé et la sauvegarder dans un fichier
def load_key():
    return open("key.key", "rb").read()

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    return key

# Charger la clé ou en générer une nouvelle si elle n'existe pas
try:
    key = load_key()
except FileNotFoundError:
    key = write_key()

f = Fernet(key)

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    try:
        valeur_bytes = valeur.encode()  # Conversion str -> bytes
        token = f.encrypt(valeur_bytes)  # Encrypt la valeur
        return f"Valeur encryptée : {token.decode()}"  # Retourne le token en str
    except Exception as e:
        return f"Erreur d'encryptage : {str(e)}"

@app.route('/decrypt/<string:token>')
def decryptage(token):
    try:
        token_bytes = token.encode()  # Conversion str -> bytes
        valeur_bytes = f.decrypt(token_bytes)  # Decrypt le token
        return f"Valeur décryptée : {valeur_bytes.decode()}"  # Retourne la valeur en str
    except Exception as e:
        return f"Erreur de décryptage : {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
