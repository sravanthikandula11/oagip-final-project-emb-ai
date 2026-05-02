"""Flask server for Emotion Detection Application"""

from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET"])
def emotion_detection():
    text_to_analyze = request.args.get("textToAnalyze")

    # Handle empty input
    if text_to_analyze is None or text_to_analyze.strip() == "":
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    result = emotion_detector(text_to_analyze)

    # Handle None dominant emotion
    if result["dominant_emotion"] is None:
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return jsonify({"response": response_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
