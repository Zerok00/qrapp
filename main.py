from flask import Flask, render_template, request
import qrcode
import os

app = Flask(__name__)

#routing
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        if os.path.isfile("../genera_qr/static/ytqr.png"):
            os.remove("../genera_qr/static/ytqr.png")
        link = request.form.get("link")
        qr = qrcode.QRCode(version=1, box_size=5, border=5)
        qr.add_data(link)
        qr.make()
        img = qr.make_image(fill_color = 'black', back_color = 'white')
        img.save("../genera_qr/static/ytqr.png")
        return render_template("home.html")
    else:
        if os.path.isfile("../genera_qr/static/ytqr.png"):
            os.remove("../genera_qr/static/ytqr.png")
        return render_template("home.html")


app.run()