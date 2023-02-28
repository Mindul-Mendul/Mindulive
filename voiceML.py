import torch
import torchaudio

print(torch.__version__)
print(torchaudio.__version__)

import io
import os
import tarfile
import tempfile

import boto3
import matplotlib.pyplot as plt
import requests
from botocore import UNSIGNED
from botocore.config import Config
from IPython.display import Audio
from torchaudio.utils import download_asset

print(str(torchaudio.get_audio_backend()))

# SAMPLE_GSM = download_asset("tutorial-assets/steam-train-whistle-daniel_simon.gsm")
# SAMPLE_WAV = download_asset("tutorial-assets/Lab41-SRI-VOiCES-src-sp0307-ch127535-sg0042.wav")
# SAMPLE_WAV_8000 = download_asset("tutorial-assets/Lab41-SRI-VOiCES-src-sp0307-ch127535-sg0042-8000hz.wav")

# metadata=torchaudio.info(SAMPLE_WAV)
# print(metadata)

# waveform, sample_rate = torchaudio.load(SAMPLE_WAV_SPEECH_PATH)

# print_stats(waveform, sample_rate=sample_rate)
# plot_waveform(waveform, sample_rate)
# plot_specgram(waveform, sample_rate)
# play_audio(waveform, sample_rate)