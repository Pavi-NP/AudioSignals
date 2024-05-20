# Audio Signal Processing Tool

<small>  This Python script processes a WAV audio file to analyze and visualize its signal. It includes functionality to identify and plot peaks (S1 and S2 sounds), 
create a spectrogram, and print various details about the audio signal.  </small>

## Features
 <small>
• Open File Dialog: Allows the user to select a WAV file from their file system. </small>

•	Audio Signal Processing:

    o	Reads the WAV file.
    o	Handles both mono and stereo audio files by averaging stereo channels.
    o	Normalizes the audio signal.
    o	Extracts and plots a segment of the audio signal.
    
•	Peak Detection: Identifies and plots peaks (S1 sounds) and valleys (S2 sounds) in the audio signal.

•	Spectrogram Creation: Generates and displays a spectrogram of the audio signal.

•	Signal Details: Prints detailed information about the audio signal, including frequency sampling, maximum and minimum amplitude, signal shape, data type, and duration. </small>


## Requirements
<small> 
  • Python 3.x   
  
  • numpy    
  
  • matplotlib  
  
  • scipy  
  
  • tkinter 
  
  </small>


## Run the script
<small> A file dialog will appear. Select a WAV file to process. </small>

## Outputs:
<img width="205" alt="image" src="https://github.com/Pavi-NP/AudioSignals/assets/148129933/b420d5fa-1b1d-4b65-bd2a-c23649805863"> </n>

<img width="356" alt="image" src="https://github.com/Pavi-NP/AudioSignals/assets/148129933/fc014d4f-7c81-4e92-873f-6f2d8124a97d"> </n>

<img width="356" alt="image" src="https://github.com/Pavi-NP/AudioSignals/assets/148129933/e6cfac10-e747-4a96-bad4-090bb1b6924d"> </n>

<img width="303" alt="image" src="https://github.com/Pavi-NP/AudioSignals/assets/148129933/477792bd-5797-40d2-929b-c61b629462eb"> </n>

Max Amplitude: 48782.7578125 

Min Amplitude: -37955.46484375 

Signal shape: 57600

Audio Signal count: (57600,) 

Signal duration: 1.2 seconds </n>







