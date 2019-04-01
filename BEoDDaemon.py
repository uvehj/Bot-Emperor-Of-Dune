import markovify
import sys
from twython import Twython
import datetime
import time

# Get raw text as string.
with open("./geod.txt") as f:
    text = f.read()


print(datetime.datetime.now())
print("Started BotEmperorOfDune daemon")


while 1 == 1:

	print(datetime.datetime.now())

	print("I sleep")
	time.sleep(15 * 60 * 60)
	print(datetime.datetime.now())
	print("Real shit")

	# Build the model.
	text_model = markovify.NewlineText(text)

	text_body = text_model.make_short_sentence(240, max_overlap_ratio = 0.5)
	if text_body != "None":
		text_body = text_body.replace(" ,", ",")
		text_body = text_body.replace(" ?", "?")
		text_body = text_body.replace(" !", "!")
		i = 0
		while len(text_body) < 110 and i < 50:
			i = i + 1
			new_text_body = text_model.make_short_sentence(110, max_overlap_ratio = 0.5)
			if new_text_body != "None":
				new_text_body = new_text_body.replace(" ,", ",")
				new_text_body = new_text_body.replace(" ?", "?")
				new_text_body = new_text_body.replace(" !", "!")
				text_body = text_body + '. ' + new_text_body

		text_body = text_body + '.'
		text_body = text_body.replace("?.", "?")
		text_body = text_body.replace("!.", ".")
		text_body = text_body.replace(",.", ",")
		if len(text_body) < 250 and i < 50:
			text_body = text_body + ' ' + "#Dune"


		apiKey = ""
		apiSecret = ""
		accessToken = ""
		accessTokenSecret = ''

		api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

		api.update_status(status=text_body)
		print(datetime.datetime.now())
		print("Tweeted: " + text_body)

	else:
		print(datetime.datetime.now())
		print("Error while creating the sentence")
