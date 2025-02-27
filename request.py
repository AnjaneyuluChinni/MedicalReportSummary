import requests
import json

URL = "http://127.0.0.1:5000/summarize"

def send_request(text):
    data = {"text": text}
    headers = {"Content-Type": "application/json"}
    response = requests.post(URL, data=json.dumps(data), headers=headers)
    
    if response.status_code == 200:
        print("Summary:", response.json()["summary"])
    else:
        print("Error:", response.json())

if __name__ == "__main__":
    sample_text = "Patient was admitted with severe chest pain and shortness of breath..."
    send_request(sample_text)