# FastAPI Machine Learning API

This project demonstrates how to deploy a machine learning model using FastAPI on a free or freemium platform. The API allows users to send input data in JSON format and receive predictions from the deployed model.

## Features
- Serve a pre-trained machine learning model via a FastAPI application.
- Accepts input data in JSON format and returns predictions.
- Deployed on a free platform (e.g., Fly.io) with CI/CD automation using GitHub Actions.

## Getting Started

### Prerequisites
- Python 3.7 or higher
- `pip` (Python package manager)
- [Fly.io CLI (`flyctl`)](https://fly.io/docs/getting-started/installing-flyctl/) for deployment

### Installation


1. Clone the Repository:

   ```bash
   git clone https://github.com/Bavanthi18/Assignment-_FastAPI
   cd Assignment_FastAPI

2.Install the Required Dependencies:
pip install -r requirements.txt

3.Run the Application Locally:
uvicorn app.main:app --reload

API Endpoints
GET /: Health check endpoint. Returns a message indicating that the API is running.

POST /predict: Endpoint to get predictions from the model.

Input: JSON object containing the required input data for the model.
Output: JSON object containing the prediction results.

Example Request
curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d '{"input_data": [5.1, 3.5, 1.4, 0.2]}'

Deployment
Install Fly.io CLI (flyctl):

Follow the instructions on Fly.io's documentation to install flyctl.

Initialize Fly.io Application:
flyctl launch


Deploy to Fly.io:
flyctl deploy


CI/CD Setup with GitHub Actions
1.Create a Workflow File:
create a file at .github/workflows/deploy.yml with the following content:
name: Deploy FastAPI to Fly.io

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'

    - name: Install dependencies
      run: |
        pip install -r requirements.txt

    - name: Deploy to Fly.io
      env:
        FLY_API_TOKEN: ${{ secrets.FLY_API_TOKEN }}
      run: |
        flyctl deploy

Add Fly.io API Token to GitHub Secrets:
Go to your GitHub repository settings, under Secrets and variables > Actions, and create a new secret named FLY_API_TOKEN with your Fly.io API token.

Testing the Deployed API
Once deployed, test your API by sending HTTP requests to the provided URL. You can use tools like curl, Postman, or any HTTP client to make requests.












## Screenshots

![Screenshot (965)](https://github.com/user-attachments/assets/123089bf-cd69-425e-a080-05472e320c94)
![Screenshot (964)](https://github.com/user-attachments/assets/b68dad02-c79a-4d68-9d4c-0373b58b9003)
![Screenshot (959)](https://github.com/user-attachments/assets/6ce5f219-791e-462f-a716-8934b24ef7f0)
![Screenshot (958)](https://github.com/user-attachments/assets/64c63e22-07f6-4a65-af3d-2b4687d975a2)
![Screenshot (957)](https://github.com/user-attachments/assets/fea9dcf5-c5ea-46d5-bcf1-cb3592050ead)
![Screenshot (978)](https://github.com/user-attachments/assets/361d768f-fa83-4667-ac4f-91c4058a4ff5)
![Screenshot (977)](https://github.com/user-attachments/assets/604c97dc-7d45-405d-bd69-27bc257fc031)
![Screenshot (976)](https://github.com/user-attachments/assets/c08df435-d9f7-443e-b4fe-0ebb05f3f16f)
![Screenshot (975)](https://github.com/user-attachments/assets/7f9f981f-5d58-45de-813a-9c5adc4a2462)
![Screenshot (974)](https://github.com/user-attachments/assets/b47c3c5d-dd9c-4a1d-a4f0-a08562aa5f10)
![Screenshot (973)](https://github.com/user-attachments/assets/9b2c5c22-1bc3-4631-8d63-ac8eef2ae3c0)
![Screenshot (972)](https://github.com/user-attachments/assets/b22264da-416b-4afc-9db2-9507cc76924a)
![Screenshot (971)](https://github.com/user-attachments/assets/d8623247-dbbb-47ee-a259-3d35fe7cf908)
![Screenshot (970)](https://github.com/user-attachments/assets/64ba06b7-e785-415a-befa-cba772624e4f)
![Screenshot (969)](https://github.com/user-attachments/assets/b5ea6b0b-2a58-49e2-984c-7f517ce1e93b)
![Screenshot (968)](https://github.com/user-attachments/assets/74e7dec2-10a6-4b4c-89ca-e3e341fc8013)
![Screenshot (967)](https://github.com/user-attachments/assets/00181f1d-b5bd-459d-9c7f-12e251c4aac9)
![Screenshot (966)](https://github.com/user-attachments/assets/d4d1700b-d1a5-4adc-9949-febaf98aeb67)