# FT: 시간 도메인의 움성 신호를 주파수 도메인으로 바꾸는 과정 // 전공 시간 때 자주 하던 거
# mag_frames: MFCC를 구할 때는 음성 인식에 불필요한 위상 정보는 없애고 진폭 정보만을 남겨야 함
# pow: Magnitude의 제곱을 N으로 나눠준 값
# 필터뱅크(Filter Banks): 저주파수 영역대를 고주파수 영역대 대비 상대적으로 세밀하게 볼 필요가 있을 때 적용하는 기법

import numpy as np

NFFT = 512 # NFFT: 나눌 도메인 구간 (보통 256이나 512 선호)

def melScaleFilter(sample_rate, frames):
  # FFT
  dft_frames = np.fft.rfft(frames, NFFT)
  mag_frames = np.absolute(dft_frames)
  pow_frames = ((1.0 / NFFT) * ((mag_frames) ** 2))

  # Mel-Scale Filter
  nfilt = 40
  low_freq_mel = 0
  high_freq_mel = (2595 * np.log10(1 + (sample_rate / 2) / 700))  # Convert Hz to Mel
  mel_points = np.linspace(low_freq_mel, high_freq_mel, nfilt + 2)  # Equally spaced in Mel scale
  hz_points = (700 * (10**(mel_points / 2595) - 1))  # Convert Mel to Hz
  bin = np.floor((NFFT + 1) * hz_points / sample_rate)

  # Filter function
  fbank = np.zeros((nfilt, int(np.floor(NFFT / 2 + 1))))
  for m in range(1, nfilt + 1):
    f_m_minus = int(bin[m - 1])   # left
    f_m = int(bin[m])             # center
    f_m_plus = int(bin[m + 1])    # right
    for k in range(f_m_minus, f_m):
      fbank[m - 1, k] = (k - bin[m - 1]) / (bin[m] - bin[m - 1])
    for k in range(f_m, f_m_plus):
      fbank[m - 1, k] = (bin[m + 1] - k) / (bin[m + 1] - bin[m])
  
  # Filter Bank
  filter_banks = np.dot(pow_frames, fbank.T) # inner product
  filter_banks = np.where(filter_banks == 0, np.finfo(float).eps, filter_banks) # Numerical Stability
  filter_banks = 20 * np.log10(filter_banks)  # dB scale
  filter_banks -= (np.mean(filter_banks, axis=0) + 1e-8) # Mean Normalization

  return filter_banks
