import math
import wave
import struct
import numpy as np
import random

filename = f"./makeFile/testWave.wav"


sample_rate = 44100.0
duration = 3.0
data_size = int(duration * sample_rate)

NFFT=512

waveValue = 0.0
sine_list_x = []
freq = np.ones(NFFT)
ampl = np.ones(NFFT)
for x in range(data_size):
    waveValue=0.0
    for i in range(0, NFFT):
        freq[i]=random.randrange(100, 1000)
        ampl[i]=random.randrange(10, 100)
        waveValue+=ampl[i]*math.sin(math.pi*freq[i]*(x/sample_rate))
    sine_list_x.append(waveValue)

wav_file = wave.open(filename, "w")

nChannels = 1
sampwidth = 2
frameRate = int(sample_rate)
nframes = data_size
comptype = "NONE"
compName = "not compressed"

wav_file.setparams((nChannels, sampwidth, frameRate, nframes, comptype, compName))

for s in sine_list_x:
    # write the audio frames to file
    if(int(s)>32768):
        print(int(s))
    if(int(s)<-23767):
        print(int(s))
    wav_file.writeframes(struct.pack('h', int(s)))

wav_file.close()