from scipy.fftpack import dct
import numpy as np

num_ceps = 12

def mfccs(filter_banks):
  mfcc = dct(filter_banks, type=2, axis=1, norm='ortho')[:, 1 : (num_ceps + 1)] # Keep 2-13

  # Lift
  (nframes, ncoeff) = mfcc.shape
  cep_lifter = 22
  n = np.arange(ncoeff)
  lift = 1 + (cep_lifter / 2) * np.sin(np.pi * n / cep_lifter)
  mfcc *= lift

def showMFCCs(mfccs):
  print(mfccs)