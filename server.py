"""Flask app for emotion detection: serves the UI and exposes an analyzer endpoint."""

from typing import Dict, Any
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

# Create Flask app with the name 'emotion_detector'
app = Flask("emotion_detector")


@app.route("/", methods=["GET"])
def render_index_page() -> str:
    """Render the main HTML page."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def analyze_emotion() -> str:
    """Analyze the provided text and return the dominant emotion as plain text.

    Returns:
        str: The dominant emotion (e.g., 'joy') or an error message when invalid.
    """
    # Retrieve the text to analyze from query parameters; default to empty string
    text_to_analyze: str = request.args.get("textToAnalyze", "")

    # Pass the text to the emotion detector
    result: Dict[str, Any] = emotion_detector(text_to_analyze)

    # Handle blank/invalid input cases per spec
    if result.get("dominant_emotion") is None:
        return "Invalid text! Please try again!"

    return str(result["dominant_emotion"])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
