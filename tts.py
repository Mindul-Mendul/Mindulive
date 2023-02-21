from gtts import gTTS
from playsound import playsound
from pydub import AudioSegment

#AudioSegment.converter= "C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe"
#AudioSegment.ffprobe="C:\\Program Files\\ffmpeg\\bin\\ffprobe.exe"

def tts(filename):
  with open(filename, "r", encoding='UTF8') as f:
    i=1
    for line in f:
      if len(line.strip())>1:
        tts=gTTS(
          text=line.strip(),
          lang='ko', slow=False
        )
        print(line.strip())
        tts.save(f'ttsFile/novel{i}.mp3')
        w=AudioSegment.from_mp3(f'ttsFile/novel{i}.mp3')
        w.export(f'ttsFile/novel{i}.wav', format='wav')
        playsound(f'ttsFile/novel{i}.wav')
        i+=1

tts("textExample/novel1.txt")
