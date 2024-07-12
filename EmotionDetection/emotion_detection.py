import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url, headers=headers, json=input_json)
    
    # Convert the response text into a dictionary
    response_json = response.json()
    
    # Extract the required set of emotions and their scores
    emotions = response_json.get('emotionPredictions', [{}])[0].get('emotion', {})
    
    # Set default values if emotions are not present in the response
    anger_score = emotions.get('anger', 0)
    disgust_score = emotions.get('disgust', 0)
    fear_score = emotions.get('fear', 0)
    joy_score = emotions.get('joy', 0)
    sadness_score = emotions.get('sadness', 0)
    
    # Find the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get, default=None)
    
    # Format the output
    output = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
    
    return output

# Testing the function
if __name__ == "__main__":
    test_text = "I love my life"
    result = emotion_detector(test_text)
    print(json.dumps(result, indent=2))
