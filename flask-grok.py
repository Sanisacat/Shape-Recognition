from flask import Flask, render_template, request
from flask_ngrok import run_with_ngrok
app = Flask(__name__)
run_with_ngrok(app)  

@app.route("/", methods=['GET', 'POST'])
def main():
  return render_template("index.html")


@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
  if request.method == 'POST':
    img = request.files['my_image']
    img_path = "static/" + img.filename 
    img.save(img_path)
    print(img_path)
    p = classify(img_path)
    return render_template("index.html", prediction = p , img_path=img_path)
app.run()
