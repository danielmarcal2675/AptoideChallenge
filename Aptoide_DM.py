# Code to obtain anomalies using flask API returning the results in JSON -22/01/2024

#Imports
from flask import Flask, jsonify
import pandas as pd
from sklearn.ensemble import IsolationForest
import sys

print("End of imports")

#Variables
dataset = pd.read_csv('transactions_dataset.csv')
app = Flask(__name__)

# Definicao do endpoint
@app.route('/anomalies_report', methods=['GET'])
def get_anomalies_report():
    # Implement anomaly detection logic in the Transaction Amount using Isolation Forest with 0.01 contamination
    isolation_forest = IsolationForest(contamination=0.01)  
    anomaly_labels = isolation_forest.fit_predict(dataset[['Transaction_Amount']])

    # Filtering out the anomalies
    anomalies = dataset[anomaly_labels == -1]

    # Convert anomalies to JSON format
    anomalies_json = anomalies.to_json(orient='records')

    # Return the JSON result
    response = {"anomalies": anomalies_json}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)


#http://127.0.0.1:5000/anomalies_report