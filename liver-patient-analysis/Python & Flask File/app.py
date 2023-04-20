import flask
from flask import Flask, render_template, request
import pickle
import numpy as np
import sklearn

app = Flask(__name__)

model1 = pickle.load(open('ETC.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/getdata', methods=['POST'])
def pred():
    age = request.form['Age']
    print(age)
    gender = request.form['Gender']
    print(age, gender)
    total_bilirubin = request.form['Total_Bilirubin']
    print(age, gender, total_bilirubin)
    direct_bilirubin = request.form['Direct_Bilirubin']
    print(age, gender, total_bilirubin, direct_bilirubin)
    alkaline_phosphotase = request.form['Alkaline_Phosphotase']
    print(age, gender, total_bilirubin, direct_bilirubin, alkaline_phosphotase)
    alamine_aminotransferase = request.form['Alamine_Aminotransferase']
    print(age, gender, total_bilirubin, direct_bilirubin, alkaline_phosphotase, alamine_aminotransferase)
    aspartate_aminotransferase = request.form['Aspartate_Aminotransferase']
    print(age, gender, total_bilirubin, direct_bilirubin, alkaline_phosphotase, alamine_aminotransferase,
          aspartate_aminotransferase)
    total_proteins = request.form['Total_Proteins']
    print(age, gender, total_bilirubin, direct_bilirubin, alkaline_phosphotase, alamine_aminotransferase,
          aspartate_aminotransferase, total_proteins)
    albumin = request.form['Albumin']
    print(age, gender, total_bilirubin, direct_bilirubin, alkaline_phosphotase, alamine_aminotransferase,
          aspartate_aminotransferase, total_proteins, albumin)
    albumin_and_globulin_ratio = request.form['Albumin_and_Globulin_Ratio']
    print(age, gender, total_bilirubin, direct_bilirubin, alkaline_phosphotase, alamine_aminotransferase,
          aspartate_aminotransferase, total_proteins, albumin, albumin_and_globulin_ratio)

    inp_features = [[int(age), int(gender), np.log(float(total_bilirubin)), np.log(float(direct_bilirubin)),
                     int(alkaline_phosphotase),
                     int(alamine_aminotransferase),
                     int(aspartate_aminotransferase),
                     np.log(float(total_proteins)), np.log(float(albumin)), np.log(float(albumin_and_globulin_ratio))]]
    print(inp_features)
    prediction = model1.predict(inp_features)
    print(type(prediction))
    t = prediction[0]
    print(t)
    if t > 0.5:
        prediction_text = 'You have a liver disease,Please consult a Doctor'
    else:
        prediction_text = 'Congratualations! You dont have a liver disease '
    print(prediction_text)
    return render_template('prediction.html', prediction_results=prediction_text)


if __name__ == "__main__":
    app.run()
