import joblib

def predict(data):
    scaler = joblib.load('./scaler.sav')
    norm_data = scaler.transform(data)
    clf = joblib.load('./svm_model.sav')
    return clf.predict(norm_data)