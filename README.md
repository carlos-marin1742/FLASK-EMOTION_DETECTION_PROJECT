# Emotion Detection Flask App

A simple Flask-based web application that detects emotions in text using IBM Watson’s **Natural Language Processing (NLP) API**.  

This project was built as part of the [IBM AI Developer Professional Certificate](https://www.coursera.org/professional-certificates/ibm-ai-developer) capstone.

---

## 🚀 Features
- Detects emotions from user-provided text (`joy`, `anger`, `sadness`, `fear`, `disgust`, etc.)
- REST API endpoint (`/emotionDetector`) that returns the **dominant emotion**
- Web interface served from `index.html`
- Includes unit tests to validate functionality

---

## 📂 Project Structure
```
FLASK-EMOTION_DETECTION_PROJECT/
│
├── EmotionDetection/
│   └── emotion_detection.py     # Emotion detection logic (Watson API wrapper)
│
├── server.py                    # Flask web server
├── test_emotion_detection.py    # Unit tests for emotion detection
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```

---

## ⚙️ Installation & Setup

1. **Clone the repo**  
   ```bash
   git clone git@github.com:carlos-marin1742/FLASK-EMOTION_DETECTION_PROJECT.git
   cd FLASK-EMOTION_DETECTION_PROJECT
   ```

2. **Create a virtual environment (recommended)**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate     # On Mac/Linux
   venv\Scripts\activate        # On Windows
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**  
   ```bash
   python server.py
   ```
   Open your browser at 👉 [http://localhost:5000](http://localhost:5000)

---

## 🔬 API Usage

**Endpoint:**  
```
GET /emotionDetector?textToAnalyze=<your text>
```

**Example:**  
```
http://localhost:5000/emotionDetector?textToAnalyze=I am so happy and excited today!
```

**Response:**  
```
"joy"
```

---

## 🧪 Running Tests
Run unit tests with:
```bash
python -m unittest test_emotion_detection.py
```

---

## 📖 Notes
- This app uses IBM Watson’s **pretrained emotion model** hosted on the Skills Network Labs.
- If you’re running outside the lab environment, make sure the Watson API endpoint is still accessible.

---

## ✨ Author
👨‍💻 Carlos Marin  
- [LinkedIn](https://www.linkedin.com/in/carlos-marin-90482b13b/)  
- [GitHub](https://github.com/carlos-marin1742)  
