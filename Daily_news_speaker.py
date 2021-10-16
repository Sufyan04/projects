# requirements to run this
#pip install pywin32
#pip install requests

import requests
import json
def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.SpVoice")
    speak.Speak(str)
def news_speaker (url):
    news=requests.get(url).text
    news_json=json.loads(news)
    arts=news_json["articles"]
    for item in arts:
        print(item["title"])
        speak(item["title"])
# you have to made a account on newsapi.org
# then copy your API and have to paste it in given below categories
# since every one have there own API link so I cant share mine
url_health="https://newsapi.org/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
url_science="https://newsapi.org/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
url_sports="https://newsapi.org/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
url_entertainment="https://newsapi.org/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"


if __name__=='__main__':
    print("choose any category:")
    print("Enter the category of news:")
    print("Press\t1 for health\n 2 for science\n 3 for sports\n 4 for entertainment.")
    x= int(input("enter here:"))
    
    if(x==1):
        speak("todays health headlines are:")
        news_speaker(url_health)
        speak("thank you for listening")
    elif(x==2):
        speak("todays science headlines are:")
        news_speaker(url_science)
        speak("thank you for listening")
    elif(x==3):
        speak("todays sports headlines are:")
        news_speaker(url_sports)
        speak("thank you for listening")
    else:
        speak("todays entertainment headlines are:")
        news_speaker(url_entertainment)
        speak("thank you for listening")
    

    