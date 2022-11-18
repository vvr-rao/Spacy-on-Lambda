# Spacy-on-Lambda


## 
Spacy model containerized to be deployed as a REST API on AWS Lambda. To install download serverless CLI. then run following commands (Linux)
1) serverless create -u https://github.com/vvr-rao/Spacy-on-Lambda -n lambda-fn
2) cd lambda-fn
3) serverless deploy (to provision Container in ECR, API Gateway endpoint & Lambda with Provisioned Concorrency)

To run, POST a message to the generated endpoint in below format:

    {
        "data": "Nothing like New York in the winter."
    }

##
VERY IMPORTANT!! REMEMBER TO RUN THE BELOW!!! 

4) servless remove  (to delete all of the above and avoid a hefty bill)

##
Model Sizes
en_core_web_sm: 13MB ; en_core_web_md: 91MB ; en_core_web_lg: 742MB

