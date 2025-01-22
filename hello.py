from flask import Flask, render_template, request, redirect
import json, os

# Flask App
template_dir = os.path.abspath("./Templates")
app = Flask(name, template_folder = template_dir)

# Events DB
EVENTS_DB = "./db/auto.json"

# Events Class
class Event:
    def init(self, auto_id, modello, targa, cilindrata, chilometraggio, anno_produzione):
        self.id = auto_id
        self.modello = modello
        self.targa = targa
        self.cilindrata = cilindrata
        self.chilometraggio=chilometraggio
        self.anno_produzione = anno_produzione
        
    def getID(self):
        return self.id
    
    def getmodello(self):
        return self.modello
    
    def getTarga(self):
        return self.targa
    
    def getcilindrata(self):
        return self.cilindrata
    
    def getChilometraggio(self):
        return self.chilometraggio
    
    def getanno_produzione(self):
        return self.anno_produzione
    
#Root / Path for Index Page at URL http://127.0.0.0:5000/
@app.route("/", methods=["GET"])
def index():
    with open(EVENTS_DB, "r") as file:
        events = json.load(file)
    
    return render_template("homepage.html", events = events)