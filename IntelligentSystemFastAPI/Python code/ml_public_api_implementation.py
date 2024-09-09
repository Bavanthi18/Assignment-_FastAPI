# -*- coding: utf-8 -*-
"""


@author: Bavanthika
"""

# -*- coding: utf-8 -*-
"""


@author: Bavanthika
"""

import json
import requests


url = 'https://ef9c-35-190-148-157.ngrok-free.app/diabetes_prediction'


input_data_for_model = {
    
    'Pregnancies' : 6,
    'Glucose' : 148,
    'BloodPressure' : 72,
    'SkinThickness' : 35,
    'Insulin' : 0,
    'BMI' : 33.6,
    'DiabetesPedigreeFunction' : 0.627,
    'Age' : 50
    
    }

input_json = json.dumps(input_data_for_model)

response = requests.post(url, data=input_json)

print(response.text)

