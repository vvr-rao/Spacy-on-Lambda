import json
import spacy

def handler(event, context):
    #read the input string
    data = json.loads(event['body'])
    data1 = json.loads(json.dumps(data))
    payload = data1['data']
    
    #INSERT NER CODE HERE
    output = 'Some Output'
    
    #return Output
    response = {"statusCode": 200, "body": output}
    return response

    
