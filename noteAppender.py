# noteAppender.py
''' 
Description: This takes a list of notes and appends the notes to different files 
based on their hashtag. 
Input: Takes a list of strings from noteParse collected by their hashtag
Output: Appends the strings to the appropriate doc file
Author: Michael Mentele
'''

def append(tag, text):
	'''Finds the file and writes text to it.'''
	myfile = open(tag[0:], "a")
	myfile.write("\n" + text)


