from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load model
model = pickle.load(open("model.pkl", "rb"))

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    X_new = np.array(data["features"]).reshape(1, -1)
    prediction = model.predict(X_new)
    return jsonify({"prediction": prediction.tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
