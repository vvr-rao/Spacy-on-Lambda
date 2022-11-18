import json
import spacy

def handler(event, context):
    #read the input string
    data = json.loads(event['body'])
    data1 = json.loads(json.dumps(data))
    payload = data1['data']
    
    #INSERT NER CODE HERE
    o = ''
    nlp2 = spacy.load("model")
    doc = nlp2(payload)
    
    for token in doc:
        o = o  +  token.text + "  " + token.pos_ + "\n"
    
    #return Output
    response = {"statusCode": 200, "body": o}
    return response

    
