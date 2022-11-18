# Spacy-on-Lambda


## 
Spacy model designed to be deployed on Lambda. To install download serverles CLI. then run following commands
1) serverless create -u https://github.com/vvr-rao/Spacy-on-Lambda -n lambda-fn
2) cd lambda-fn
3) serverless deploy (should provision Container in ECR, API Gateway,  Lambda with Provisioned Concorrency)

To run, POST a message in below format:
{
    "data": "Nothing like New York in the winter."
}

##
VERY IMPORTANT!! REMEMBER TO RUN THE BELOW!!! 

4) servless remove  (to delete all of the above and avoid a hefty bill)

##
Model Sizes
en_core_web_sm: 13MB Size of en_core_web_md: 91MB Size of en_core_web_lg: 742MB

