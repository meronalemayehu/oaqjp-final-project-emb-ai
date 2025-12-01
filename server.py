"""
Flask web server for the Emotion Detection application

This file provides routes to render the home page and to process 
emotion detection requests using Watson NLP-based emotion detector.
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    """
    Render the main index page of the web app

    Returns:
        str: Rendered HTML template for the home page.
    """
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detector_route():

    """"
    Handle emotion detection requests from the client

    Retrieves the input text from the request, sends it to the 
    emotion detector, and reutrns the formatted result.

    Returns:
        str: Formatted emotion analysis result or an error message.
    """

    text_to_analyze = request.args.get("textToAnalyze")

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:

        return "Invalid text! Please try again!"

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']}, "
        f"'sadness': {result['sadness']}, "
        f"The dominant emotion is {result['dominant_emotion']}. "
    )

    return response_text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
