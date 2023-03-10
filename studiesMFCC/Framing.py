# Framing - 시그널을 쪼개는 작업
# 이유: raw wave signal 데이터는 빠르게 변화함, 분석 시간 구간이 길면 정보 캐치가 어렵고 처리할 때 왜곡이 커짐(non-stationary)
# Framing을 통해 음성 시그널을 구간마다 stationary하게 만듦

import numpy as np

# frame_size: 한 프레임 당 시간. 보통 20ms~40ms
# frame_stride: 프레임마다 겹치는 시간. // windowing을 위함
frame_size = 0.025 # 25ms
frame_stride = 0.01 # 10ms

def frame(emphasized_signal, sample_rate):
  frame_length, frame_step = frame_size * sample_rate, frame_stride * sample_rate
  signal_length = len(emphasized_signal)
  frame_length = int(round(frame_length))
  frame_step = int(round(frame_step))
  num_frames = int(np.ceil(float(np.abs(signal_length - frame_length)) / frame_step))
  pad_signal_length = num_frames * frame_step + frame_length
  z = np.zeros((pad_signal_length - signal_length))
    
  # pad_signal: emphasized_signal에 제로패딩z를 이어붙인 것
  # indices: pad_signal에서 인덱스 기준으로 값을 참조하기 위해 만든 변수
  # indices와 frame의 shape = 행*열 에서 행은 프레임 개수, 열은 frame 하나의 길이
  pad_signal = np.append(emphasized_signal, z)
  indices = np.tile(np.arange(0, frame_length), (num_frames, 1)) + \
    np.tile(np.arange(0, num_frames * frame_step, frame_step), (frame_length, 1)).T
  frames = pad_signal[indices.astype(np.int32, copy=False)]

  # windowing: 각각의 프레임에 특정 함수를 적용해 경계를 스무딩하는 기법
  # Hamming window: smoothing을 위해 사용하는 filter 함수 (수식은 복잡해서 코드 내에 있는 것으로 대체)
  frames *= np.array([0.54 - 0.46 * np.cos((2 * np.pi * n) / (frame_length - 1)) for n in range(frame_length)])

  return frames  