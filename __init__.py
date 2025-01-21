from cryptography.fernet import Fernet
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/base_svg')
def base_svg():
    return render_template('base_svg.html')

@app.route('/maison')
def maison():
    return render_template('maison.html')

@app.route('/valet')
def valet():
    return render_template('valet.html')

@app.route('/chenille')
def chenille():
    return render_template('chenille.html')

@app.route('/d6f')
def d6f():
    return render_template('d6f.html')
    
# Route pour chiffrer une valeur avec une clé privée manuelle
@app.route('/encrypt/<string:key>/<string:valeur>')
def encryptage(key, valeur):
    try:
        f = Fernet(key.encode())  # Crée un objet Fernet avec la clé fournie
        valeur_bytes = valeur.encode()  # Conversion str -> bytes
        token = f.encrypt(valeur_bytes)  # Chiffrement de la valeur
        return f"Valeur encryptée : {token.decode()}"  # Retourne le token en str
    except Exception as e:
        return f"Erreur : {str(e)}", 400

# Route pour déchiffrer une valeur avec une clé privée manuelle
@app.route('/decrypt/<string:key>/<string:encrypted_val>')
def decryptage(key, encrypted_val):
    try:
        f = Fernet(key.encode())  # Crée un objet Fernet avec la clé fournie
        encrypted_bytes = encrypted_val.encode()  # Conversion str -> bytes
        decrypted_text = f.decrypt(encrypted_bytes).decode()  # Déchiffrement
        return f"Valeur décryptée : {decrypted_text}"
    except Exception as e:
        return f"Erreur : {str(e)}", 400

if __name__ == "__main__":
    app.run(debug=True)
