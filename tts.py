from gtts import gTTS
from playsound import playsound

# import pyttsx3
# AudioSegment.converter="C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe"
# AudioSegment.ffprobe="C:\\Program Files\\ffmpeg\\bin\\ffprobe.exe"
# engine = pyttsx3.init()
# engine.setProperty('rate',180)

def tts(filename):
  i=1
  with open(filename, "r", encoding='UTF8') as f:
    for line in f:
      if len(line.strip())>1:
        tts=gTTS(
          text=line.strip(),
          lang='ko', slow=False
        )
        print(line.strip())
        try:
          soundFileName='./ttsFile/'+filename[filename.rindex('/'):filename.rindex('.')]+f'{i}.mp3'
          tts.save(soundFileName)
          playsound(soundFileName)
          i+=1
        except:
          print("file extension is not found")
        
tts('./textExample/example.txt')