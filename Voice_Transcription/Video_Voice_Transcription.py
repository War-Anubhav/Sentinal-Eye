from transformers import pipeline
import librosa
import numpy as np
import pandas as pd
from moviepy.editor import VideoFileClip

whisper_transcribe = pipeline("automatic-speech-recognition", model="openai/whisper-large-v3")

video_file_path = 'C:/Users/aranu/Desktop/Minor_Combined/Input_Data/Video.mp4'

video_clip = VideoFileClip(video_file_path)
audio_file_path = 'C:/Users/aranu/Desktop/Minor_Combined/Input_Data/Audio_Generated.wav'
video_clip.audio.write_audiofile(audio_file_path, codec='pcm_s16le') 

audio_data, samplerate = librosa.load(audio_file_path, sr=16000)
chunk_length_samples = 5 * samplerate
num_chunks = int(np.ceil(len(audio_data) / chunk_length_samples))
word_counts = []

for i in range(num_chunks):
    start_sample = i * chunk_length_samples
    end_sample = start_sample + chunk_length_samples
    audio_chunk = audio_data[start_sample:end_sample]
    
    if audio_chunk.size > 0:
        result = whisper_transcribe(audio_chunk)
        text = result['text']
        print(f"Chunk {i+1} Transcribed: {text[:50]}...") 
        num_words = len(text.split())
        word_counts.append(num_words / 5)  

df_word_counts = pd.DataFrame(word_counts, columns=['Word_Count_Per_Second'])
csv_file_path = 'C:/Users/aranu/Desktop/Minor_Combined/Voice_Transcription/word_counts.csv'
df_word_counts.to_csv(csv_file_path, index=False)

print(f"Word counts for each chunk saved to {csv_file_path}")
