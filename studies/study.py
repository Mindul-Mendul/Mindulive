import scipy.io.wavfile

# sample_rate: 초당 샘플링 개수 [Hz]
# signal은 array로 반환. 길이는 샘플링된 각각의 값.
# signal.dtype: 시그널의 비트 수. int16이면 16bits로 양자화 되어있는 것
# len(signal)/sample_rate: 음성의 길이 (해당 값이 11.455면 음성파일이 11.455초짜리 음성이라는 뜻)
# signal[int(a*sample_rate):int(b*sample_rate)]: signal을 a~b초 사이를 자르는 방법

sample_rate, signal = scipy.io.wavfile.read('./studies/test.wav')
time = len(signal) / sample_rate # 전체 signal의 길이 [s]
signal = signal[0:int(3.5 * sample_rate)] # 0s ~ 3.5s로 자름

# print(sample_rate) 
# print(signal.dtype)
# print(time)
# print(len(signal)/sample_rate)

# Preemphasis
from Preemphasis import preemphasis

emphasized_signal = preemphasis(signal=signal)

# Framing
from Framing import frame

frames = frame(emphasized_signal, sample_rate)

# Filter Banks
from FilterBanks import melScaleFilter

filter_banks = melScaleFilter(sample_rate, frames)

# MFCCs
from MFCCs import mfccs

mfcc=mfccs(filter_banks)