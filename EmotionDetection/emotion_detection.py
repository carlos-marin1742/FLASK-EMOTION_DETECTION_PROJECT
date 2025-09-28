import requests 
import json

def emotion_detector(text_to_analyze):
    #URL of the sentiment analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    #Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyze } }
    #Custom header specifying the model ID for the emotion detection service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Sending a POST request to the emotion detection API
    response = requests.post(url, json = myobj, headers = header)
    #parsing JSON reponse
    response_json = json.loads(response.text)

    none_result = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    }
    #handling blank input or errors
    if response.status_code == 400:
        return none_result
    
    try:
        #extracting emotion scores
        emotions = response_json['emotionPredictions'][0]['emotion']
        
        #emotional scores
        anger_score = emotions['anger']
        disgust_score = emotions['disgust']
        fear_score = emotions['fear']
        joy_score = emotions['joy_score']
        sadness_score = emotions['sadness']

        #determining dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)
        
        result = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
        }

        return result
    
    except:
        return none_result