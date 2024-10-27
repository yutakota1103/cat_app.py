from flask import Flask, jsonify, send_file
import requests
from PIL import Image
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def show_cat():
    # 猫画像APIからURLを取得
    cats_url = "https://api.thecatapi.com/v1/images/search"
    res = requests.get(cats_url)
    cat_url = res.json()[0]["url"]

    # 画像データをダウンロード
    response = requests.get(cat_url)
    img = Image.open(BytesIO(response.content))

    # 画像をBytesIOで保存してFlaskで送信
    img_io = BytesIO()
    img.save(img_io, 'JPEG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/jpeg')

if __name__ == "__main__":
    app.run(debug=True)
