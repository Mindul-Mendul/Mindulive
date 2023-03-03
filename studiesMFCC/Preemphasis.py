# preemphasis: 고주파 성분의 에너지를 올려주는 전처리 과정.
# 사람 말소리를 Spectrum으로 변환해서 관찰하면 일반적으로 저주파 성분의 에너지가 고주파보다 많은 경향이 있음

# 하는 이유 - 고주파 성분의 에너지를 조금 올려주면 음성 인식 모델의 성능을 개선할 수 있다고 함
# 1. 상대적으로 에너지가 적은 고주파 성분을 강화함으로써 원시 음성 신호가 전체 주파수 영역대에서 비교적 고른 에너지 분포를 갖도록 함.
# 2. 푸리에 변환시 발생할 수 있는 numerical problem 예방.
# 3. Signal-to-Noise Ratio(SNR) 개선.

# 수식: y(t)=x(t)-α*x(t-1)
# Preemphasis coefficient α 는 보통 0.95나 0.97을 사용

import numpy as np

def preemphasis(signal):
  pre_emphasis = 0.97
  emphasized_signal = np.append(signal[0], signal[1:] - pre_emphasis * signal[:-1])
  return emphasized_signal

