import nltk
import numpy as np
dataset=[]

weather= {
 "What's the weather like":"getWeather",
 "How's the weather":"getWeather",
 "Nice weather, isn't it ":"getWeather",
 "Terrible weather, isn't it":"getWeather",
 "It's a nice day, isn't it":"getWeather",
 "Tell me how is the weather":"getWeather",
 "Tell me that weather is nice today":"getWeather",
 "Is weather nice today":"getWeather",
 "How's the weather today":"getWeather",
 "Is weather rainy today":"getWeather",
 "Is it rainy":"getWeather",
 "Is weather sunny today":"getWeather",
 "Is it sunny?":"getWeather",
 "Is it windy":"getWeather",
 "Is weather windy":"getWeather",
 "I like sunny weather":"nope",
 "I like walking in the rain":"nope",
 "I don't trust weather forecasts":"nope",
 "Weather is snowy today":"nope",
 "Weather is nice":"nope",
 "It is rainy":"nope",
 "It is sunny":"nope",
 "Sunny weathers that i love":"nope",}
message={
 "can you send message to my friend":"sendMessage",
 "please send message to":"sendMessage",
 "I need to send message to":"sendMessage",
 "Could you send message to":"sendMessage",
 "Let's send message":"sendMessage",
 "I would like to send message":"sendMessage",
 "what about send message":"sendMessage",
 "can you deliver message to my friend":"sendMessage",
 "please deliver message":"sendMessage",
 "I need to deliver message":"sendMessage",
 "Could you deliver message to":"sendMessage",
 "Let's deliver message to":"sendMessage",
 "I would like to deliver message to":"sendMessage",
 "what about deliver message":"sendMessage",
 
 "can you send sms to my friend":"sendMessage",
 "please send sms to":"sendMessage",
 "I need to send sms to":"sendMessage",
 "Could you send sms to":"sendMessage",
 "Let's send sms":"sendMessage",
 "I would like to send sms":"sendMessage",
 "what about send sms":"sendMessage",
 "can you deliver sms to my friend":"sendMessage",
 "please deliver sms":"sendMessage",
 "I need to deliver sms":"sendMessage",
 "Could you deliver sms to":"sendMessage",
 "Let's deliver sms to":"sendMessage",
 "I would like to deliver sms to":"sendMessage",
 "what about deliver sms":"sendMessage",
 "Write to":"sendMessage",
 "can you write sms ":"sendMessage",
 "please write message":"sendMessage",
 "could you write message":"sendMessage",
 "write sms":"sendMessage",
 "I would like to check my messages":"nopeMessage",
 "I hate recieving messages":"nopeMessage",
 "Filter spam messages":"nopeMessage",
 "Is there any new message":"nopeMessage",
 "Read last message for me":"nopeMessage",
 "don't send message":"nopeMessage",
 "cancel message":"nopeMessage",
 "stop message":"nopeMessage",
 "I would like to check my sms":"nopeMessage",
 "I hate recieving sms":"nopeMessage",
 "Filter spam sms":"nopeMessage",
 "Is there any new sms":"nopeMessage",
 "Read last sms for me":"nopeMessage",
 
}
mail={
"send Mail to":"sendMail",
"can you send mail to and say":"sendMail",
"could you write a letter to ":"sendMail",
"can you write mail and say":"sendMail",
"I need you to send mail":"sendMail",
"I need you to write letter":"sendMail",
"can you send letter to":"sendMail",
"can you write mail":"sendMail",
"could you send letter to":"sendMail",
"could you write mail for me":"sendMail",
"I would like to send mail to":"sendMail",
"I would like to write mail":"sendMail",
"Can you deliver mail to and say":"sendMail",
"I need you deliver this mail":"sendMail",
"can you write letter and say":"sendMail",
"can you deliver this mail to":"sendMail",
"let's write some letter":"sendMail",
"I would like to check my mails":"nopeMail",
"I hate spam mails":"nopeMail",
"Is there any new mail for me":"nopeMail",
"can you read my last mail":"nopeMail",
"can you check my mails":"nopeMail",
"filter spam mails":"nopeMail",
"can you read last mail for me":"nopeMail",
"can you filter spams":"nopeMail",
"delete mails":"nopeMail",
"delete all letters":"nopeMail",

}
call={
"can you call":"call",
"call":"call",
"make a call":"call",
"call please":"call",
"can you make a call":"call",
"could you call":"call",
"I need to call":"call",
"let's call":"call",
"I need to speak with":"call",
"I want to speak with":"call",
"I will call":"call",
"I will speak with":"call",
"can you dial":"call",
"dial":"call",
"could you dial":"call",
"dial for me":"call",
"can dial for me":"call",

"I hate they calling me all time":"nopeCall",
"Did anyone called me":"nopeCall",
"I will call the police":"nopeCall",
"Please don't call me":"nopeCall",
"They didn't called me ":"nopeCall",
"Did I called":"nopeCall",
"Stop calling me":"nopeCall",
}
BFF={
"is my best friend":"BFF",
"my best friend is":"BFF",
"make my best friend":"BFF",
"is my bff":"BFF",
"my bff is":"BFF",
"make my bff":"BFF",
"save as my best friend":"BFF",
"save as my bff":"BFF",
}
testPositive={
"how is weather":"getWeather",
"I would like to know weather":"getWeather",
"send a message for me":"sendMessage",
"I would like to send mail":"sendMail",
"Eren Demir is my best firend":"BFF",
"Call Alper":"call",
"How is weather today":"getWeather",
"can you call mom":"call",
"write a sms to Eren Demir":"sendMessage",
"Give me weather report now":"getWeather"
}
testNegative={
"I like snowy weather":"nope",
"don't send message":"nopeMessage",
"do i have any message":"nopeMessage",
"Is there any call for me":"nopeCall",
"can you check my mails":"nopeMail",
"I hate spam mails":"nopeMail",
"I like walking in the rain":"nope"

}
testMixed={
"call my best friend":"call",
"I'd like to now weather":"getWeather",
"dial Eren":"call",
"write a letter for me and say ok i will deal with it":"sendMail",
"write a message to mom and say i am ok":"sendMessage",
"It is snowy today":"nope",
"I hate spam mails":"nopeMail",
"Is there any messages for me":"nopeMessage",
"delete last message":"nopeMessage",
"Did anyone called me":"nopeCall"
}

def getDataSet():
    for key, value in weather.items():
            temp = [key,value]
            dataset.append(temp)
    for key, value in message.items():
            temp = [key,value]
            dataset.append(temp)
    for key, value in call.items():
            temp = [key,value]
            dataset.append(temp)
    for key, value in mail.items():
            temp = [key,value]
            dataset.append(temp)
    for key, value in BFF.items():
            temp = [key,value]
            dataset.append(temp)
    
    return dataset
def getpositive():
        ds=[]
        for key,value in testPositive.items():
                temp=[key,value]
                ds.append(temp)
        return ds
def getnegative():
        ds=[]
        for key,value in testNegative.items():
                temp=[key,value]
                ds.append(temp)
        return ds
def getmixed():
        ds=[]
        for key,value in testMixed.items():
                temp=[key,value]
                ds.append(temp)
        return ds

