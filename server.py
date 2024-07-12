from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detection_analysis():
    """
    Analyzes the emotion of the provided text.
    
    Query Params:
    - textToAnalyze: The text to analyze for emotions.
    
    Returns:
    - A string with the emotion scores and the dominant emotion.
    """
    text = request.args.get("textToAnalyze")
    response = emotion_detector(text)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    if dominant_emotion is None:
        return "Invalid text! Please try again!."

    return (
        f"For the given statement, the system response is 'anger':"
        f"{anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}."
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Renders the index page.
    
    Returns:
    - The rendered HTML of the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
