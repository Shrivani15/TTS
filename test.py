from gtts import gTTS 
  
# import Os module to start the audio file
import os 

fh = open("test.txt", "r")
myText = fh.read().replace("\n", " ")

# Language we want to use 
language = 'en'

output = gTTS(text=myText, lang=language, slow=False,tld="com.au")

output.save("output1.mp3")
fh.close()

# Play the converted file 
os.system("start output1.mp3")