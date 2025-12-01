import requests
import json


def emotion_detector(text_to_analyze):
    # call Watson NLP EmotionPredict endpoint
    url = ("https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict")


    # Set the headers
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
        }

    #create payload with the text to be analyzed
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 400:

        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None 
        }

    #convert json text to python dictionary
    response_dict = json.loads(response.text)

    #navigate to the emotions dictionary
    emotions = response_dict["emotionPredictions"][0]["emotion"]

    anger = emotions["anger"]
    disgust = emotions["disgust"]
    fear = emotions["fear"]
    joy = emotions["joy"]
    sadness = emotions["sadness"]

    #find the dominant emotion
    emotion_scores = {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
    }

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    #return output
    result = {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
        "dominant_emotion": dominant_emotion,
    }
        


