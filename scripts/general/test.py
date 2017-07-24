import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn

def course_code(sentence):
	try:
		words = re.compile('\w+').findall(sentence)
		new_sentence = ""
		for index, word in enumerate(words):
			if (word == "cs") and (index < len(words)-1) and (words[index+1].isdigit()):
				new_sentence = new_sentence + word
			else:
				new_sentence = new_sentence + word + " "
		return new_sentence
	except:
		return sentence

#http://pythonprogramming.net/part-of-speech-tagging-nltk-tutorial/?completed=/stemming-nltk-tutorial/
dict = {'NN': 'NOUN', 'JJ': 'ADJ'}
dict['NNS'] = 'NOUN'
dict['NNP'] = 'NOUN'
dict['NNPS'] = 'NOUN'
dict['PRP'] = 'NOUN'
dict['PRP$'] = 'NOUN'
dict['RB'] = 'ADV'
dict['RBR'] = 'ADV'
dict['RBS'] = 'ADV'
dict['VB'] = 'VERB'
dict['VBD'] = 'VERB'
dict['VBG'] = 'VERB'
dict['VBN'] = 'VERB'
dict['VBP'] = 'VERB'
dict['VBZ'] = 'VERB'
dict['WRB'] = 'ADV'

# pos tag -> morphy -> synset
# Morphy take NOUN,VERB,ADV,ADJ
while True:
	sentence = raw_input(">> ")
	sentence = sentence.lower()
	sentence = course_code(sentence)
	stop_words = set(stopwords.words('english'))
	word_tokens = word_tokenize(sentence)

	filtered_sentence = [w for w in word_tokens if not w in stop_words]
	print filtered_sentence
	temp = nltk.pos_tag(filtered_sentence)
	
	new_sentence = ""
	for i in temp:
		try:
			k = i[1]
			if (dict[k] != None):
				part_speech = dict[k]
			else:
				part_speech = 'NOUN'

			if(part_speech == 'NOUN'):
				word = wn.morphy(i[0],wn.NOUN)
			elif(part_speech == 'VERB'):
				word = wn.morphy(i[0],wn.VERB)
			elif(part_speech == 'ADV'):
				word = wn.morphy(i[0],wn.ADV)
			elif(part_speech == 'ADJ'):
				word = wn.morphy(i[0],wn.ADJ)
			word1 = wn.synsets(word)[0].lemmas()[0].name()
		except:
			word1 = i[0]
		new_sentence = new_sentence+" "+word1.lower()
	print type(new_sentence)
	print new_sentence