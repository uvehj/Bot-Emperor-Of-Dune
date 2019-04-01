#Creates and prints a tweet, doesn't send it

import markovify

# Get raw text as string.
with open("./geod.txt") as f:
    text = f.read()

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
	print(text_body)
