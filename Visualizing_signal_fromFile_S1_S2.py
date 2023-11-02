#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 00:51:26 2023

@author: paviprathiraja

"""
#------------------------

#Visualizing Audio Signals - Select a file and read it
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import find_peaks
from scipy.signal import spectrogram
import tkinter as tk
from tkinter import filedialog

#-----------------------

def open_file_dialog():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    file_path = filedialog.askopenfilename(
        title="Select a WAV file",
        filetypes=[("WAV files", "*.wav"), ("All files", "*.*")]
    )

    if file_path:
        process_wave_file(file_path)

def process_wave_file(file_path):


# Read the WAV file
    frequency_sampling, audio_signal = wavfile.read(file_path)
    
    
    # If the audio signal has multiple channels (stereo), take the average
    if audio_signal.ndim == 2:
        audio_signal = np.mean(audio_signal, axis=1)
        
        audio_signal = audio_signal / np.power(2, 15)
        
        #audio_signal = audio_signal [0:28800]
        #audio_signal = audio_signal [28800:57600]
        #audio_signal = audio_signal [57600:86400]
        audio_signal = audio_signal [28800:86400]
        #audio_signal = audio_signal [0:86400]
        
        #audio_signal = audio_signal [28800:56400]
        
        time_axis = 1000 * np.arange(0, len(audio_signal), 1) / float(frequency_sampling)
        
    peaks, _ = find_peaks(audio_signal, height=1000)  # Adjust the height threshold based on your signal
        
    
    #-----------
    
    plt.plot(time_axis, audio_signal, color='red')
    plt.xlabel('Time (millisecond)')
    plt.ylabel('Amplitude')
    plt.title('Input audio signal')
    plt.grid(True)
    plt.show()
#-----------------

        # Plot the entire audio signal
    plt.figure(figsize=(10, 6))
    plt.subplot(2, 1, 1)
    plt.plot(audio_signal)
    plt.title("Original Audio Signal")
        
        # Plot S1 (lub) peaks
    plt.subplot(2, 1, 2)
    plt.plot(audio_signal)
    plt.plot(peaks, audio_signal[peaks], "x", label="S1 Peaks")
    plt.title("S1 (lub) Peaks")
    plt.xlabel("Sample Index")
    plt.ylabel("Amplitude")
    plt.legend()
        
    plt.tight_layout()
    plt.show()
        
        #----------------
        
        
    # Identify valleys between peaks as potential S2 (dub) locations
    valleys, _ = find_peaks(-audio_signal, height=-1000)  # Adjust the height threshold based on your signal
    
    # Plot the entire audio signal
    plt.figure(figsize=(10, 6))
    plt.subplot(2, 1, 1)
    plt.plot(audio_signal)
    plt.title("Original Audio Signal")
    
    # Plot S1 (lub) peaks
    plt.subplot(2, 1, 2)
    plt.plot(audio_signal)
    plt.plot(peaks, audio_signal[peaks], "x", label="S1 Peaks")
    plt.plot(valleys, audio_signal[valleys], "o", label="S2 Peaks")
    plt.title("S1 (lub) and S2 (dub) Peaks")
    plt.xlabel("Sample Index")
    plt.ylabel("Amplitude")
    plt.legend()
    
    plt.tight_layout()
    plt.show()

  #-------------
  # If the audio signal has multiple channels (stereo), take the average
    if audio_signal.ndim == 2:
              audio_signal = np.mean(audio_signal, axis=1)
    
    print('\nFrequency Sampling:', frequency_sampling, 'Hz')

    frequencies, times, spectrogram_data = spectrogram(audio_signal, fs=frequency_sampling)

#---------------
# Create a spectrogram
#frequencies, times, spectrogram_data = spectrogram(audio_signal, fs=frequency_sampling)

    # Plot the spectrogram
    plt.figure(figsize=(10, 6))
    plt.pcolormesh(times, frequencies, 10 * np.log10(spectrogram_data), shading='auto')
    plt.title("Spectrogram")
    plt.xlabel("Time (s)")
    plt.ylabel("Frequency (Hz)")
    plt.colorbar(label="Power/Frequency (dB/Hz)")
    plt.show()



 #-------------
    max_amplitude = audio_signal.max()
    min_amplitude = audio_signal.min()
    
    print('Max Amplitude:', max_amplitude)
    print('Min Amplitude:', min_amplitude)
    
    
    print('\nSignal shape:', audio_signal.shape[0])
    print('\nAudio Signal count:', audio_signal.shape)
    
    print('Signal Datatype:', audio_signal.dtype)
    print('Signal duration:', round(audio_signal.shape[0] / 
    float(frequency_sampling), 2), 'seconds')
    
   
    print('\nTime axis:', time_axis, 'millisecond') 



#---------------
# Open the file dialog when running the script
open_file_dialog()


