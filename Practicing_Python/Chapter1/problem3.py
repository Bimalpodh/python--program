import pyttsx3
import speech_recognition as sr

recognizer=sr.Recognizer()
engine=pyttsx3.init()

with sr.Microphone() as source:
  print("say somthing....")
  audio=recognizer.listen(source)
  
  try:
    text=recognizer.recognize_google(audio)
    engine.say("you said",text)
    engine.runAndWait()
  except sr.UnknownValueError :
    print("could not understand")
  except sr.RequestError:
        print("Could not request results from Google Speech Recognition service")
    



