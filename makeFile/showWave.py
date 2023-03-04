#%%
import matplotlib.pyplot as plt
import librosa
import librosa.display

# 파일 불러오기
x, sr = librosa.load('./makeFile/WaveTest.wav')

# 파형 그래프(wave graph)
FIG_SIZE=(15, 10)
plt.figure(figsize=FIG_SIZE)
librosa.display.waveshow(x, sr=sr)

# short time Fourier transform graph (spectrogram)
# cast amplitude to decibels (apply logarithm)
X = librosa.stft(x)
Xdb = librosa.amplitude_to_db(abs(X))
plt.figure(figsize=(14, 5))
librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')
plt.colorbar()

# MFCCS
## Extract 13 MFCCs
n_fft=2048
hop_length=512

# 그림 그리기
plt.show()
