from flask import Flask, render_template, request, redirect
import db, cgi, json, urllib, urllib2

app = Flask(__name__)
app.secret_key = 'insert_clever_secret_here'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cards",methods=['GET','POST'])
def handleCardsRequest():
    if request.method=='GET':
        return json.dumps(db.getCards())
    else:
        return `db.addCard(request.json['name'],request.json['company'])`

@app.route("/cards/<cardID>",methods=['DELETE'])
def handleCardRequest(cardID):
    if request.method=="DELETE":
        return `db.deleteCard(cardID)`
    
if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5000)
