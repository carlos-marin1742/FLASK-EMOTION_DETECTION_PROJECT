# Emotion Detection Flask App
Flask based web-application that detects emotions in text using IBM's Watson's Natural Language Processing (NLP) API.

This Probject was built as part of the IBM AI Developer Certificate Capstone

### Features
 - Detects emotions from user-provided text('joy', 'anger', 'sadness','fear', etc.)
 - REST API endpoint (/emotionDetector) that returns the dominant emotion
 - Web interface served from index.html
 - includes unit texts to validate functionality

 ### Project structure
 FLASK-EMOTION_DETECTION_PROJECT/

├── EmotionDetection/
│   └── emotion_detection.py     # Emotion detection logic (Watson API wrapper)

├── server.py                    # Flask web server

├── test_emotion_detection.py    # Unit tests for emotion detection

├── requirements.txt             # Python dependencies

└── README.md                    # Project documentation

## Installation & set up
#### 1. Clone the repo
git clone git@github.com:carlos-marin1742/FLASK-EMOTION_DETECTION_PROJECT.git
cd FLASK-EMOTION_DETECTION_PROJECT


<div style="background: #1a1a1a; color: #00ff00; padding: 15px; border-radius: 5px; font-family: 'Courier New', monospace;">
  <span style="color: #ffff00;">$</span> git clone git@github.com:carlos-marin1742/FLASK-EMOTION_DETECTION_PROJECT.git<br>
  <span style="color: #ffff00;">$</span> cd FLASK-EMOTION_DETECTION_PROJECT
</div>


#### 2. create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate     # On Mac/Linux
venv\Scripts\activate        # On Windows

#### 3. install dependecies
pip install -r requirements.txt

### 4. run the app. 
pip install -r requirements.txt

Open the browser at  http://localhost:5000