from flask import Flask, request
from generate import generate_image
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    img_path = None
    if request.method == "POST":
        prompt = request.form.get("prompt")
        img_path = f"images/{prompt[:10].replace(' ', '_')}.png"
        os.makedirs("images", exist_ok=True)
        generate_image(prompt, img_path)
    return f'''
        <h2>AI 图像生成器</h2>
        <form method="post">
            <input name="prompt" placeholder="输入文字生成图片"/>
            <button type="submit">生成</button>
        </form>
        {'<img src="'+img_path+'" width="400"/>' if img_path else ''}
    '''

if __name__ == "__main__":
    app.run(debug=True)