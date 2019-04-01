#Waits a set amount of time, tweets and rinse and repeat

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
	#As of now the time to wait is hardcoded here
	time.sleep(15 * 60 * 60)
	print(datetime.datetime.now())
	print("Real shit")

	# Build the model.
	text_model = markovify.NewlineText(text)

	#Creates the first sentence, max characters to the twitter max
	text_body = text_model.make_short_sentence(240, max_overlap_ratio = 0.5)
	if text_body != "None":
		#Removes blanks preceding characters (the only 3 that appear in the text)
		text_body = text_body.replace(" ,", ",")
		text_body = text_body.replace(" ?", "?")
		text_body = text_body.replace(" !", "!")
		i = 0
		#If the sentence is too short adds more sentences to get to at least half the max characters
		while len(text_body) < 110 and i < 50:
			i = i + 1
			new_text_body = text_model.make_short_sentence(110, max_overlap_ratio = 0.5)
			if new_text_body != "None":
				new_text_body = new_text_body.replace(" ,", ",")
				new_text_body = new_text_body.replace(" ?", "?")
				new_text_body = new_text_body.replace(" !", "!")
				text_body = text_body + '. ' + new_text_body

		#Final period and removal of unnecessary periods
		text_body = text_body + '.'
		text_body = text_body.replace("?.", "?")
		text_body = text_body.replace("!.", ".")
		text_body = text_body.replace(",.", ",")
		
		#If there is space it adds a generic Dune hashtag
		if len(text_body) < 250 and i < 50:
			text_body = text_body + ' ' + "#Dune"


		#Here be the twitter keys, don't make them public (I know this is not the safest way to go about it)
		apiKey = ""
		apiSecret = ""
		accessToken = ""
		accessTokenSecret = ''

		api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

		#Send tweet
		api.update_status(status=text_body)
		print(datetime.datetime.now())
		print("Tweeted: " + text_body)

	else:
		#In case the sentence generation goes wrong
		print(datetime.datetime.now())
		print("Error while creating the sentence")
