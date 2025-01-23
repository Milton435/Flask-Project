from flask import Flask, render_template, request, redirect, jsonify
import json
import os


template_dir = os.path.abspath("./Templates")
app = Flask(__name__, template_folder=template_dir)


EVENTS_DB = "./db/auto.json"



class Event:
    def __init__(self, car_id, model, numberPlate, displacement, mileage, YOProduction, price):
        self.id = car_id
        self.model = model
        self.numberPlate = numberPlate
        self.displacement = displacement
        self.mileage = mileage
        self.YOProduction = YOProduction
        self.price = price

    def to_dict(self):
        return {
            "carid": self.id,
            "model": self.model,
            "numberPlate": self.numberPlate,
            "displacement": self.displacement,
            "mileage": self.mileage,
            "YOProduction": self.YOProduction,
            "price": self.price,
        }



def load_events():
    if not os.path.exists(EVENTS_DB):
        return []
    with open(EVENTS_DB, "r") as file:
        return json.load(file)


def save_events(events):
    with open(EVENTS_DB, "w") as file:
        json.dump(events, file, indent=4)



@app.route("/", methods=["GET"])
def index():
    return render_template("homepage.html")

@app.route("/bugatti")
def bugatti(): 
    events = load_events()
    return render_template("bugatti.html", events=events)




@app.route("/add_car", methods=["POST"])
def add_car():
    events = load_events()
    new_car_data = request.json

    new_event = Event(
        car_id=len(events) + 1,
        model=new_car_data["model"],
        numberPlate=new_car_data["numberPlate"],
        displacement=new_car_data["displacement"],
        mileage=new_car_data["mileage"],
        YOProduction=new_car_data["YOProduction"],
        price=new_car_data["price"],
    )

    events.append(new_event.to_dict())
    save_events(events)
    return jsonify({"message": "Car added successfully"}), 201


@app.route("/edit_price", methods=["POST"])
def edit_price():
    events = load_events()
    data = request.json
    car_id = int(data["carid"])
    new_price = data["price"]

    for car in events:
        if car["carid"] == car_id:
            car["price"] = new_price
            break

    save_events(events)
    return jsonify({"message": "Price updated successfully"}), 200


@app.route("/delete_car/<int:car_id>", methods=["DELETE"])
def delete_car(car_id):
    events = load_events()
    updated_events = [car for car in events if car["carid"] != car_id]

    if len(events) == len(updated_events):
        return jsonify({"message": "Car not found"}), 404

    save_events(updated_events)
    return jsonify({"message": "Car deleted successfully"}), 200



if __name__ == "__main__":
    app.run(debug=True)
