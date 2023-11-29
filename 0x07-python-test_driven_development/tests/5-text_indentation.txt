import the function:
	>>> text_indentation = __import__('5-text_indentation').text_indentation

text str
	>>> text_indentation("my name is salma")
	my name is salma

text str?
	>>> text_indentation("whats that? ok no problem")
	whats that?
	<BLANKLINE>
	ok no problem

text str.
	>>> text_indentation("my name is salma. iam 32 years old")
	my name is salma.
	<BLANKLINE>
	iam 32 years old

text str:
	>>> text_indentation("they said: oh no!")
	they said:
	<BLANKLINE>
	oh no!

text number
	>>> text_indentation(32)
	Traceback (most recent call last):
	TypeError: text must be a string
