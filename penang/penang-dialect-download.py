# browse thru youtube videos and identify the most genuine state dialects
# copy the links
# run the script to download the audio files only (mp3 format which to be save in "download" folder)

import ssl
import os
import ffmpeg

ssl._create_default_https_context = ssl._create_unverified_context


link1="https://youtu.be/_K8Wbd2IHxY"
link2="https://youtu.be/48Jz-_jKVV4"
link3="https://youtu.be/kP_-Fa4nIWw"
link4="https://youtu.be/ZOy07PPKMuo"
link5="https://youtu.be/M2yCEcetLcI"
link6="https://youtu.be/OBY0W4UfE5s"
link7="https://youtu.be/gx_a7E9c3Uw"
link8="https://youtu.be/mPGjcszJOT8"
link9="https://youtu.be/JdIdUHPfaUI"
link10="https://youtu.be/6vKjn59VtWo"

links=[link1,link2,link3,link4,link5,link6,link7,link8,link9,link10]

for link in links:
    os.system("youtube-dl -x --audio-format mp3 --no-check-certificate --verbose "+link)
    os.system("mv *.mp3 ./download")

