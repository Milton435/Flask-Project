from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista di elementi con titolo e URL immagine
items = [
    {'title': 'Audi', 'url': 'https://www.google.com/imgres?q=audi%20sq8&imgurl=https%3A%2F%2Fcdn.motor1.com%2Fimages%2Fmgl%2F49Obq%2Fs1%2Faudi-sq8-by-abt.webp&imgrefurl=https%3A%2F%2Fit.motor1.com%2Fnews%2F378963%2Faudi-sq8-abt-diesel%2F&docid=IiN9vUgo9H3iyM&tbnid=_3gOw0p3OTOD_M&vet=12ahUKEwihg82G_oOLAxWHhP0HHeffBGsQM3oECBgQAA..i&w=1920&h=1080&hcb=2&ved=2ahUKEwihg82G_oOLAxWHhP0HHeffBGsQM3oECBgQAA'}
]

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Ottieni i dati dal form
        new_item_title = request.form.get('new_item_title')
        new_item_url = request.form.get('new_item_url')
        
        # Controlla che i campi siano validi
        if new_item_title and new_item_url:
            # Aggiungi il nuovo elemento
            items.append({'title': new_item_title, 'url': new_item_url})
        return redirect(url_for('home'))  # Ricarica la pagina per mostrare i nuovi dati
    return render_template('/templates/bugatti.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)

