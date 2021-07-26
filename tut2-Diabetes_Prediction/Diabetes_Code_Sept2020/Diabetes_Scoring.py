import os
import sys 
import json
import requests
from time import sleep


'''
Pregnancies - Number of times pregnant 
Glucose — The blood plasma glucose concentration after a 2 hour oral glucose tolerance test.
BloodPressure — Diastolic blood pressure (mm/HG).
SkinThickness — Skinfold thickness of the triceps (mm).
Insulin — 2 hour serum insulin (mu U/ml).
BMI — Body mass index (kg/m squared)
DiabetesPedigreeFunction — A function that determines the risk of type 2 diabetes based on family history, the larger the function, the higher the risk of type 2 diabetes.
Age.

Example input 
{ 
	"use_scoring": true, 
	"scoring_args": {
		"NumPreg" : 8.0, 
		"Glucose" : 183.0, 
		"BloodPressure" : 64.0, 
		"SkinThick" : 0.0, 
		"Insulin" : 0.0, 
		"BMI" : 23.3, 
		"DiabetesPedFunc" : 0.672, 
		"Age" : 32.0
	}
}

'{"NumPreg":1.0,"Glucose":85.0,"BloodPressure":66.0,"SkinThick":29.0,"Insulin":0.0,"BMI":26.6,"DiabetesPedFunc":0.351,"Age":35.0}'

'''

cli_input = json.loads(sys.argv[1])
features = [] 
col_names = ["NumPreg", "Glucose", "BloodPressure", "SkinThick", "Insulin", "BMI", "DiabetesPedFunc", "Age"]
for i in col_names:
	features.append(cli_input[i])
payload = {
	"instances": [features, features]
}

r = requests.post('http://localhost:8051/v1/models/diabetes-prediction:predict', json=payload)
pred = json.loads(r.content.decode('utf-8'))['predictions'][0]
pred = round(pred[0] * 100,2)

#print("Chances of having diabetes: " + str(pred) + "%")
print(str(pred))
