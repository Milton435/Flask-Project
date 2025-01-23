from flask import Flask, render_template, request, redirect
import json, os

# Flask App
template_dir = os.path.abspath("./Templates")
app = Flask(__name__, template_folder = template_dir)

# Events DB
CAR_DB = "./db/auto.json"

# Events Class
class Event:
    def init(self, car_id, model, numberPlate, displacement, mileage, YOProduction):
        self.id = car_id
        self.model = model
        self.numberPlate = numberPlate
        self.displacement = displacement
        self.mileage=mileage
        self.YOProduction = YOProduction
        
    def getID(self):
        return self.id
    
    def getmodello(self):
        return self.model
    
    def getTarga(self):
        return self.numberPlate
    
    def getcilindrata(self):
        return self.displacement
    
    def getChilometraggio(self):
        return self.mileage
    
    def getanno_produzione(self):
        return self.YOProduction
    
#Root / Path for Index Page at URL http://127.0.0.0:5000/
@app.route("/", methods=["GET"])
def index():
    with open(CAR_DB, "r") as file:
        events = json.load(file)
    
    return render_template("homepage.html", events = events)


@app.route("/add", methods=["GET", "POST"])
def add_event():
    if request.method == 'POST':
        with open(CAR_DB, "r") as file:
            events = json.load(file)
            
        new_event = Event(
            car_id = len(events) + 1,
            model = request.form["model"],
            numberPlate = request.form["numberPlate"],
            displacement= request.form["displacement"],
            mileage = request.form["mileage"],
            YOProduction = request.form["YOProduction"]
        )
        
        events.append(new_event._dict_)
        
        with open(CAR_DB, 'w') as file:
            json.dump(events, file, indent=4)
        
        return redirect('/')
        
    return render_template('bugatti.html')