import speech_recognition as sr

r = sr.Recognizer()
def recognizeLive():
  with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
    try:
      print("You said: " + r.recognize_google(audio, language='ko-KR'))
    except sr.UnknownValueError:
      print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
      print("Could not request results from Google Speech Recognition service; {0}".format(e))

recognizeLive()