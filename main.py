from flask import Flask, render_template, request
import qrcode
import os
from io import BytesIO

app = Flask(__name__, static_folder="static")

#routing
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        if os.path.exists("/app/static/ytqr.png"):
            os.chmod("/app/static/ytqr.png", 0o666)
        os.chmod("/app/static", 0o666)
        link = request.form.get("link")

        qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)
        qr.add_data(link)
        qr.make()

        img = qr.make_image(fill_color = 'black', back_color = 'white')
        img.save("/app/static/ytqr.png")
        
        return render_template("home.html")
    else:
        if os.path.exists("/app/static/ytqr.png"):
            os.chmod("/app/static/ytqr.png", 0o666)
            os.remove("/app/static/ytqr.png")
        return render_template("home.html")


app.run(host="0.0.0.0", port=int("5000"), debug=True)