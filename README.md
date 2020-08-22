# pip install moviepy

# video-to-audio-converter-python
MoviePy can read and write all the most common audio and video formats, including GIF, and runs on Windows/Mac/Linux, with Python 2.7+ and 3 (or only Python 3.4+ from v.1.0). Here it is in action in an IPython notebook


MoviePy (full documentation) is a Python library for video editing: cutting, concatenations, title insertions, video compositing (a.k.a. non-linear editing), video processing, and creation of custom effects. See the gallery for some examples of use.

# Example
In this example we open a video file, select the subclip between t=50s and t=60s, add a title at the center of the screen, and write the result to a new file:

from moviepy.editor import *

video = VideoFileClip("myHolidays.mp4").subclip(50,60)

# Make the text. Many more options are available.
txt_clip = ( TextClip("My Holidays 2013",fontsize=70,color='white')
             .set_position('center')
             .set_duration(10) )

result = CompositeVideoClip([video, txt_clip]) # Overlay text on video
result.write_videofile("myHolidays_edited.webm",fps=25) # Many options...

# Installation

MoviePy depends on the Python modules Numpy, imageio, Decorator, and tqdm, which will be automatically installed during MoviePy’s installation. The software FFMPEG should be automatically downloaded/installed (by imageio) during your first use of MoviePy (installation will take a few seconds). If you want to use a specific version of FFMPEG, follow the instructions in config_defaults.py. In case of trouble, provide feedback.

Installation by hand: download the sources, either from PyPI or, if you want the development version, from GitHub, unzip everything into one folder, open a terminal and type:

$ (sudo) python setup.py install

Installation with pip: if you have pip installed, just type this in a terminal:

$ (sudo) pip install moviepy
