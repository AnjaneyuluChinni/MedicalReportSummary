# Medical Text Summarization API

This is a Flask-based API for summarizing medical reports using a fine-tuned T5 model.

## 🚀 Features
- Summarizes lengthy medical texts into concise summaries.
- Provides a web interface for user interaction.
- Exposes a REST API for integration with other applications.

## 📂 Project Structure
```
├── medical_summary_model/   # Saved fine-tuned model
├── templates/
│   ├── index.html           # Web interface for summarization
├── app.py                   # Flask application
├── request.py               # Script to test API requests
├── requirements.txt         # Required dependencies
├── Procfile                 # Heroku deployment configuration
├── runtime.txt              # Specifies Python version (For Heroku)
└── README.md                # Documentation
```

## 🔧 Installation
```bash
pip install -r requirements.txt
```

## 🎯 Running the App Locally
```bash
python app.py
```
Access the web interface at: `http://127.0.0.1:5000/`

## 📡 API Usage
### Endpoint: `/summarize`
**Method:** `POST`

**Request Format:**
```json
{
  "text": "Patient was admitted with severe chest pain and shortness of breath..."
}
```

**Response Format:**
```json
{
  "summary": "Patient admitted with chest pain and breathlessness."
}
```

## 🚀 Deployment
### **Deploying on Render**
1. Push the project to GitHub.
2. Create a **New Web Service** on [Render](https://render.com/).
3. Set **Build Command:**
   ```bash
   pip install -r requirements.txt
   ```
4. Set **Start Command:**
   ```bash
   gunicorn app:app
   ```
5. Deploy and get your API live!

### **Deploying on Heroku**
```bash
git init
git add .
git commit -m "Initial commit"
heroku login
heroku create medical-summary-api
git push heroku main
heroku ps:scale web=1
heroku open
```

## 📌 Notes
- Ensure `medical_summary_model/` is uploaded before deployment.
- Use **Postman** or **cURL** to test API requests.

## 🛠 Tech Stack
- **Flask** (Backend Framework)
- **Hugging Face Transformers** (T5 Model)
- **Torch** (Deep Learning Library)
- **HTML, JavaScript** (Web Interface)
- **Render/Heroku** (Deployment)

## 🤝 Contributing
Feel free to open issues or submit pull requests for improvements.

## 📜 License
This project is open-source and available under the MIT License.
