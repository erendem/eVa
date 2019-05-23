from flask import Flask,jsonify,make_response,request
import nltk
import DataSet
import Train
import random
from nltk.tokenize import word_tokenize
import pandas as pd
from nltk.tag import StanfordNERTagger
app = Flask(__name__)

ds = DataSet.getDataSet()
all_words = set(word.lower() for passage in ds for word in word_tokenize(passage[0]))
ds = [({word: (word in word_tokenize(x[0])) for word in all_words}, x[1]) for x in ds]
tr = Train.Train(ds,all_words)
tr.fit2()

@app.route('/classify', methods=['POST'])
def get_function():
    sentence= request.get_json() #request.args.get('p')
    sentence = str(sentence["sent"])
    print(sentence)
    function = tr.predict(sentence)
    print(function)
    st = StanfordNERTagger('english.all.3class.distsim.crf.ser.gz','stanford-ner.jar',encoding='utf-8')
    tokenized_text = word_tokenize(sentence)
    classified_text = st.tag(tokenized_text)
    person=""
    for x,y in classified_text:
        if(y=="PERSON"):
            person=x
    message=""
    if(" say " in sentence):
        index = sentence.find("say")
        message = sentence[index+4:]
    if(function!="BFF"):
        if(" best friend " in sentence):
            person="BFF"
        if(" bff " in sentence):
            person="BFF"
    response={"nope":"Come Again"}
    if(function=="getWeather"):
        response={str(function):""}
        
    elif(function=="call"):
        response={str(function):str(person)}

    elif(function=="sendMessage"):
        response={str(function):{str(person):str(message)}}

    elif(function=="sendMail"):
        response={str(function):{str(person):str(message)}}
    elif(function=="BFF"):
        response={str(function):str(person)}
    else:
        response={"nope":"Tell me again please."}

    return jsonify(response)
if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=8080)