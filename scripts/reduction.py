import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn
import re

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
		
def remove_aiml_char(sentence):
	try:
		new_sentence = sentence.replace("_","")
		new_sentence = new_sentence.replace("*","")
		return new_sentence
	except:
		return sentence

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

grade_codes = ["ap","aa","ab","bb","bc","cc","cd","dd","dx","fr"]

# pos tag -> morphy -> synset
# Morphy take NOUN,VERB,ADV,ADJ

# number of concepts on which the query is based 
NUM_CONCEPTS = 	13
# run loop from num = 0,1,2--- NUM_CONCEPTS-1
for num in range(8,NUM_CONCEPTS):
	if num == 0:
		concept = "prof"
	if num == 1:
		concept = "credits"
	if num == 2:
		concept = "syllabus"
	if num == 3:
		concept = "title"
	if num == 4:
		concept = "studentstrength"
	if num == 5:
		concept = "venue"
	if num == 6:
		concept = "gradeAP"
	if num == 7:
		concept = "grades"		
	if num == 8:
		concept = "duration"
	if num == 9:
		concept = "prerequisites"
	if num == 10:
		concept = "homepage"
	if num == 11:
		concept = "type"
	if num == 12:
		concept = "references"
	raw_query_path = "raw_query/raw_query_"+concept
	reduced_query_path = "reduced/reduced_"+concept
	f = open(raw_query_path,'r')
	g = open(reduced_query_path,'w')
	
	for line in f:
		sentence = line[:-1]
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
					part_speech = 'NOUN' #default is noun

				if(part_speech == 'NOUN'):
					word = wn.morphy(i[0],wn.NOUN)
				elif(part_speech == 'VERB'):
					word = wn.morphy(i[0],wn.VERB)
				elif(part_speech == 'ADV'):
					word = wn.morphy(i[0],wn.ADV)
				elif(part_speech == 'ADJ'):
					word = wn.morphy(i[0],wn.ADJ)

				word1 = wn.synsets(word)[0].lemmas()[0].name()
				if i[0] in grade_codes:
					word1 = i[0]
			except:
				word1 = i[0]
			if new_sentence == "":
				new_sentence = new_sentence + word1.lower()
			else:
				new_sentence = new_sentence+" "+word1.lower()
		new_sentence = remove_aiml_char(new_sentence)
		print new_sentence
		g.write(new_sentence+"\n")

	f.close()
	g.close()
#---------------------------------------------------------------------------

