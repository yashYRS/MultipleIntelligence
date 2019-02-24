import librosa
import librosa.display
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.signal import butter, lfilter

def function play():
    refSample, samplerrate = librosa.load("C:/Users/hp/Desktop/SIH/SoundProcessing/middlecsample.wav",duration=5)
    sd.play(refSample,samplerate=samplerate)
    return refSample, samplerate

def function record(samplerrate, refShape):
    rec = sd.rec(5*samplerate,samplerate=samplerate,channels=1,blocking=True)
    rec = np.reshape(rec,refShape)
    return rec


def function butter_lowpass(cutoff, fs, order=6):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a


def function butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y


def function getResult(refSample, recSample, samplerate, level):
    DrefSample = librosa.core.stft(refSample)
    frequencyRefSample = np.max(np.abs(DrefSample))
    
    #set cutoffs
    lower_cutoff = 0
    upper_cutoff =0
    if level == 1:
        lower_cutoff = frequencyRefSample - 100.0
        upper_cutoff = frequencyRefSample + 100.0
    else if level == 2
        lower_cutoff = frequencyRefSample - 50.0
        upper_cutoff = frequencyRefSample + 50.0
    else:
        lower_cutoff = frequencyRefSample - 25.0
        upper_cutoff = frequencyRefSample + 25.0
        
    
    filtered_rec = butter_lowpass_filter(recSample, upper_cutoff, samplerate, order=6)
    filtered_rec = butter_lowpass_filter(filtered_rec, lower_cutoff, samplerate, order=6)
    
    DrecSample = librosa.core.stft(filtered_rec)
    frequencyRecSample = np.max(np.abs(DrecSample))
    
    if frequencyRecSample >= lower_cutoff and frequencyRecSample <= upper_cutoff:
        msg = "Well done you guessed correct."
    else if: frequencyRecSample <= lower_cutoff:
        msg = "That was too low"
    else:
        msg = "That was too high."
        
    return msg

    
    