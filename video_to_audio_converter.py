# pip install moviepy

import moviepy.editor as me

# file location

file=input("Enter Your Video File Path: ")
video= me.VideoFileClip(file)

audio=video.audio

# video to audio conversation

audio.write_audiofile("new_audio.mp3")

input()
