#noteParser.py
'''
3.5.x
Description: This module splits a note up into its #tag and its text.
Author: Michael Mentele
'''
import re

def parseText(note):
	'''Parses a string into its hashtag and textstring.'''
	try:
		hashtag_idx = note.index('#')
	except ValueError:
		raise Exception('No hashtag in note!')

	hashtag = note[hashtag_idx:]
	text = note[:hashtag_idx]

	return [hashtag, text]

