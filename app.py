from flask import Flask, request, jsonify, rende_template
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    notas_float = [float(x) for x in request.form.values()]
    nota_final = [np.array(notas_float)]
    pred = model.predict(nota_final)
    output = round(prediciton[0], 2)
    return render_template('index.html', prediction_text='A classificacao prevista é: {}'.format(output))

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.get_json(force=True)
    prediciton = model.predict([np.array(list(data.values()))])
    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
    