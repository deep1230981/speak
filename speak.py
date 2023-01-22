from gtts import gTTS
msg = 'Hey deep the black hacker'
language = 'en'
obj =gTTS(text=msg, lang=language, slow=False)
obj.save('virus.mp4')
for i in range(5):
	os.system('mpg321 virus.mp4')