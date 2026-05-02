import requests

def emotion_detector(text_to_analyze):
    if text_to_analyze is None or text_to_analyze.strip() == "":
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    json_input = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, json=json_input, headers=headers)

    if response.status_code == 200:
        formatted_response = response.json()

        anger = formatted_response["emotionPredictions"][0]["emotion"]["anger"]
        disgust = formatted_response["emotionPredictions"][0]["emotion"]["disgust"]
        fear = formatted_response["emotionPredictions"][0]["emotion"]["fear"]
        joy = formatted_response["emotionPredictions"][0]["emotion"]["joy"]
        sadness = formatted_response["emotionPredictions"][0]["emotion"]["sadness"]

        emotion_scores = {
            "anger": anger,
            "disgust": disgust,
            "fear": fear,
            "joy": joy,
            "sadness": sadness
        }

        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        emotion_scores["dominant_emotion"] = dominant_emotion

        return emotion_scores

    else:
        return {"error": "Unable to fetch emotion data"}
