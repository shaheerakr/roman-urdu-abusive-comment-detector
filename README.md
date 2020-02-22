# roman-urdu-abusive-comment-detector
detects abusive comments
## to use this code
* clone this repository</br>
* install tensorflow</br>
* install keras</br>
* install genism</br>
* load the model deep.h5</br>
* load word2vec model using pickle from wv.pickle</br>
* convert the sentence into vectors using the getVector function in deep.py</br>
* make pridictions using the loaded deep learing model of the converted vector</br>

## How to use REST API
### URL
* API is deployed on heroku at: https://roman-urdu.herokuapp.com/api/uuid
* uuid should be replaced by an request id (any number) eg: 123
### Request
* Only POST method is allowed
* uuid must be specified in url
* The content-type key must specify as application/json in headers like: "Content-Type": "application/json"
* The request should have a json object which should have a key "sentences" which should contain list of sentences in roman urdu
* a curl request is given below
```
curl -d '{"sentences":["tum ache insan ho","tu ha kia pagal?"]}' -H "Content-Type: application/json" -X POST http://roman-urdu.herokuapp.com/api/123
```
### Response
* The response will have a key uuid which will have the same uuid which was provided in the url
* The response will have a key results which will have a list of predictions (abusive/not abusive) with the original sentences
* the response of above curl request is given below
```
{"results":[{"prediction":"not abusive","sentence":"tum ache insan ho"},{"prediction":"abusive","sentence":"tu ha kia pagal?"}],"uuid":"123"}
```
