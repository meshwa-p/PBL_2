import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt


audio_path = "/Users/meshu/Downloads/Sample.wav"
signal, sr = librosa.load(audio_path, sr=None)


mfcc = librosa.feature.mfcc(y=signal, sr=sr, n_mfcc=20)

# Print shape
print("MFCC Shape:", mfcc.shape)

# Plot MFCC
plt.figure(figsize=(10, 4))
librosa.display.specshow(mfcc, x_axis='time')
plt.colorbar()
plt.title('MFCC Feature Representation')
plt.tight_layout()
plt.show()