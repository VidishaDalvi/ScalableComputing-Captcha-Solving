import os
from pydub import AudioSegment

os.chdir("C:/TCD/DS/Scalable_Computing/Lab_Project3/new2/audio/")

audio_files = os.listdir()

# picking up mp3 audio files in the folder 
for file in audio_files:
    name, ext = os.path.splitext(file)
    if ext == ".mp3":
       mp3_sound = AudioSegment.from_mp3(file)
       #saving the wav files
       mp3_sound.export("{0}.wav".format(name), format="wav")