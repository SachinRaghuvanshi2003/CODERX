from flask import Flask,render_template,request,jsonify
from flask_cors import CORS
from flask import redirect
from chat import get_response
from starcoder import query
import sqlite3
app=Flask(__name__)
CORS(app)
@app.route("/",methods=["GET"])
def index_get():
    return render_template("base.html")
@app.route("/predict",methods=["POST"])
def predict():
    text=request.get_json().get("message")
    response=get_response(text)
    message={"answer":response}
    return jsonify(message)
@app.route("/codeplayground",methods=["GET"])
def get_code():
    return render_template("codeplayground.html")
@app.route("/playlist",methods=["GET"])
def get_playlist():
    return render_template("playlist.html")
@app.route("/codeplayground",methods=["POST"])
def generate():
    text=request.form.get("gentext")
    input=text
    output=query({"inputs":input})
    return render_template("codeplayground.html",output=input+output[0]['generated_text'])
@app.route("/compiler",methods=["GET"])
def getcompiler():
    return render_template("compiler.html")
@app.route("/codingpractice",methods=["GET"])
def test():
    return redirect("https://leetcode-clone-youtube-beta.vercel.app/")
@app.route("/mentalhealthsurvey",methods=["GET"])
def test2():
    return render_template("survey.html")
@app.route("/community",methods=["GET"])
def test12():
    return redirect("https://thunderous-flan-4b9c0d.netlify.app/")
@app.route("/gethelp",methods=["GET"])
def test121():
    return render_template("gethelp.html")
@app.route("/collab",methods=["GET"])
def test1223():
    return redirect("https://coderx-collab.onrender.com/")
@app.route("/documentation",methods=["GET"])
def test12234():
    return render_template("index.html")
@app.route("/frontend.html",methods=["GET"])
def test122345():
    return render_template("frontend.html")
@app.route("/backend-tech.html",methods=["GET"])
def test122346():
    return render_template("backend-tech.html")
@app.route("/programmiLang.html",methods=["GET"])
def test122347():
    return render_template("programmiLang.html")
@app.route("/devspace",methods=["GET"])
def test12235():
    return redirect("http://127.0.0.1:8000/")
@app.route("/voicecommunity",methods=["GET"])
def y12():
    return redirect("https://wondrous-licorice-0380a2.netlify.app/")
if __name__=="__main__":
    app.run(debug=True)

