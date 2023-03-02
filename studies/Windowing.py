# windowing: 각각의 프레임에 특정 함수를 적용해 경계를 스무딩하는 기법
# Hamming window: smoothing을 위해 사용하는 filter 함수 (수식은 복잡해서 코드 내에 있는 것으로 대체)

import numpy as np

def window(frames, frame_length):
    return frames * np.array([0.54 - 0.46 * np.cos((2 * np.pi * n) / (frame_length - 1)) for n in range(frame_length)])

