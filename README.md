# kuzuri.AI is a Not So really AI who talks to you listen coomand at it's  optimum.
Feel free to fork , pull ,edit the repo and at the same time looking forward to make this more robust. 

Speech recognition engine/API support:

CMU Sphinx (works offline)
Google Speech Recognition
Google Cloud Speech API
Wit.ai
Microsoft Azure Speech
Microsoft Bing Voice Recognition (Deprecated)
Houndify API
IBM Speech to Text
Snowboy Hotword Detection (works offline)

https://www.state.gov/wp-content/uploads/2021/06/AI-Motherboard-scaled.jpg

Requirements
To use all of the functionality of the library, you should have:

Python 2.6, 2.7, or 3.3+ (required)
PyAudio 0.2.11+ (required only if you need to use microphone input, Microphone)
PocketSphinx (required only if you need to use the Sphinx recognizer, recognizer_instance.recognize_sphinx)
Google API Client Library for Python (required only if you need to use the Google Cloud Speech API, recognizer_instance.recognize_google_cloud)
FLAC encoder (required only if the system is not x86-based Windows/Linux/OS X)
The following requirements are optional, but can improve or extend functionality in some situations:

On Python 2, and only on Python 2, some functions (like recognizer_instance.recognize_bing) will run slower if you do not have Monotonic for Python 2 installed.
If using CMU Sphinx, you may want to install additional language packs to support languages like International French or Mandarin Chinese.
