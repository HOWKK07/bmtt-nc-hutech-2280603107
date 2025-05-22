from flask import Flask, Request, jsonify
from cipher.caesar import Caesar

app = Flask(__name__)
caesar = Caesar()
@app.route("/api/caesar/encrypt", methohs = ["POST"])
def encrypt():
    data = Request.json
    plain = data["plain"]
    key = int(data["key"])
    encrypted = caesar.encrypted_text(plain, key)
    return jsonify({'encrypted_message': encrypted})
@app.route("/api/caesar/decrypt", methohs = ["POST"])
def decrypt():
    data = Request.json
    plain = data["cipher"]
    key = int(data["key"])
    decrypted = caesar.encrypted_text(plain, key)
    return jsonify({'decrypted_message': decrypted})
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug= True)