from flask import Flask, render_template, request
import qrcode
import os
from io import BytesIO

app = Flask(__name__, static_folder="static")

#routing
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        link = request.form.get("link")
        qr = qrcode.make(link)
        encoded = BytesIO()
        qr.save(encoded)
        bytes_enc = encoded.getvalue() #conversione sbagliata
        stringa = "data:image/png; base64," + str(bytes_enc)
        print(bytes_enc)
        return render_template("home.html", encoded=stringa)
    else:
        return render_template("home.html")


app.run(host="0.0.0.0", port=int("5000"), debug=True)