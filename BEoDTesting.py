#Creates and prints a tweet, doesn't send it

import markovify

# Get raw text as string.
with open("./geod.txt") as f:
    text = f.read()

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
print(text_body)
