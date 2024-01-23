# Aptoide Challenge

Hello Aptoide World!

Thank you for the challenge.

My experience with flask is very slim, so I tried to do my best possible.

In this code, we can find an anomalie detector in the Transaction Amount of the given dataset. Using Isolation Forest from sklearn:

### In the first step we define the contamination level desired to solve our problem using the algorithm.
    isolation_forest = IsolationForest(contamination=0.01)  
    anomaly_labels = isolation_forest.fit_predict(dataset[['Transaction_Amount']])

### After we can filter out the anomalies
    anomalies = dataset[anomaly_labels == -1]

### Then we convert anomalies to JSON format as asked
    anomalies_json = anomalies.to_json(orient='records')

### And in the end we return the JSON result
    response = {"anomalies": anomalies_json}
    return jsonify(response)

## Afterwards the results will be displayed here -> http://127.0.0.1:5000/anomalies_report

Thank you so much one more time for this amazing challenge, feel free to check the code at any time!
