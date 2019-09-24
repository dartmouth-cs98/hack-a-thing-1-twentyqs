#!/usr/bin/env python
# coding: utf-8

# In[1]:


import speech_recognition as sr
import pyttsx3


# In[2]:


def getResponse(trait, isHe):
    if isHe:
        instructions = 'Is he ' + trait
    else:
        instructions = 'Is he good at ' + trait
    
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-50)
    engine.say(instructions)
    engine.runAndWait()
    
    recog = sr.Recognizer()
    mic = sr.Microphone()
        
    while True:
        # Referenced https://realpython.com/python-speech-recognition/
        
        with mic as source:
            # recog.adjust_for_ambient_noise(source, duration=0.1)
            audio = recog.listen(source)

        response = {
            "success": True,
            "error": None,
            "transcription": None
        }

        # try recognizing the speech in the recording
        # if a RequestError or UnknownValueError exception is caught,
        #     update the response object accordingly
        try:
            response["transcription"] = recog.recognize_google(audio)
        except sr.RequestError:
            # API was unreachable or unresponsive
            response["success"] = False
            response["error"] = "API unavailable"
        except sr.UnknownValueError:
            # speech was unintelligible
            response["error"] = "Unable to recognize speech"
        
        if response["error"]:
            print("ERROR: {}".format(response["error"]))
            break
        
        if response["transcription"] == 'yes':
            engine.say('Your answer is yes.')
            engine.runAndWait()
            return True
        
        if response["transcription"] == 'no':
            engine.say('Your answer is no.')
            engine.runAndWait()
            return False
        
        engine.say('Sorry I did not get that, please answer yes or no.')
        engine.say(instructions)
        engine.runAndWait()