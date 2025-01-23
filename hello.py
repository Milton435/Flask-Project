from flask import Flask, render_template, request, redirect
import json, os

# Flask App
template_dir = os.path.abspath("./Templates")
app = Flask(__name__, template_folder = template_dir)

# Events DB
CAR_DB = "./db/auto.json"

# Events Class
class Car:
    def _init_(self, car_id, model, numberPlate, displacement, mileage, YOProduction):
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
        cars = json.load(file)
    
    return render_template("homepage.html", cars = cars)


@app.route("/add", methods=["GET", "POST"])
def add_event():
    if request.method == 'POST':
        with open(CAR_DB, "r") as file:
            cars = json.load(file)
            
        new_car = {
            "id": request.form["carId"],
            "model": request.form["model"],
            "numberPlate": request.form["numberPlate"],
            "displacement": request.form["displacement"],
            "mileage": request.form["mileage"],
            "YOProduction": request.form["YOProduction"],
        }
        
        cars.append(new_car)
        
        with open(CAR_DB, 'w') as file:
            json.dump(cars, file, indent=4)
        
        return redirect('/')
        
    return render_template('bugatti.html')