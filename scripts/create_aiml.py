import re
#-----------------------------------------------------------------------------------
g = open('cs344.aiml','w')

COURSECODE = "344"
PROFESSOR = "G. Shivakumar"
CREDITS = "6"
SYLLABUS = "Search, Logic, Constraint Programming, Neural Networks"
TITLE = "Introduction to Artificial Intelligence"
STUDENTSTRENGTH = "95"
VENUE = "LH 301"
VENUE1 = "Lecture Hall 301"
TIMESLOT = "2A"
#for AP,AA,AB,BB,BC,CC,CD,DD,DX,FR
GRADES = ["1","9","14","35","21","2","2","8","0","3"]
grade_index={'AP':0,'AA':1,'AB':2,'BB':3,'BC':4,'CC':5,'CD':6,'DD':7,'DX':8,'FR':9}
REFERENCES = "Norvig Artificial Intelligence"
TYPE = "Theory"
DURATION = "Full Semester"
HOMEPAGE = "www.moodle.iiitnr.ac.in/course"
PREREQUISITES = "None"
#-----------------------------------------------------------------------------------

def add_underscore(sentence):
	try:
		words = re.compile('\w+').findall(sentence)
		new_sentence = ""
		for index, word in enumerate(words):
			if new_sentence == "":
				new_sentence = word
			else:
				new_sentence = new_sentence + " _ "+ word
		return new_sentence
	except:
		return sentence
#--------------------prof---------------------------------------------------------------------------
f = open('reduced/reduced_prof','r')
# omit empty lines and lines containing only whitespace
lines = [line for line in f if line.strip()]
f.close()
lines.sort()


header = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>" + "\n" + "<aiml version=\"1.0\">"
g.write(header+"\n\n")

lines = list(set(lines))
for line in lines:
	sentence = line[:-1]
	new_sentence = sentence.upper()
	for i in [0,1]:
		if i == 0:	
			sentence = add_underscore(new_sentence)
		else:
			sentence = new_sentence
		new_line = ""
		s = "<category>"
		new_line = new_line + s + "\n"
		s = "\t" + "<pattern>"+sentence+"</pattern>"
		new_line = new_line + s + "\n"
		s = "\t" + "<template><srai>INSTRUCTOR "+COURSECODE+"</srai></template>"
		new_line = new_line + s + "\n"
		s = "</category>"
		new_line = new_line + s + "\n"
		g.write(new_line+"\n")

s = "<!-- answers -->"+"\n"
s = s + "<category>\n"
s = s + "\t"+"<pattern>INSTRUCTOR "+COURSECODE+"</pattern>"+"\n"
s = s + "\t<template>\n" + "\t\t<random>\n"
s = s + "\t\t\t<li>$Professor "+PROFESSOR+" is teaching CS"+COURSECODE+". </li>\n"
s = s + "\t\t\t<li>$Professor "+PROFESSOR+" will be teaching CS"+COURSECODE+". </li>\n"
s = s + "\t\t\t<li>$Instructor of CS"+COURSECODE+" is Professor "+PROFESSOR+". </li>\n"
s = s + "\t\t\t<li>$CS"+COURSECODE+" is running under instruction of Professor "+PROFESSOR+". </li>\n"
s = s + "\t\t</random>\n" + "\t</template>\n"+"</category>\n"
new_line = s
g.write(new_line+"\n")
#-------------------------prof ends------------------------------------------------------------------

#--------------------------credits--------------------------------------------------------------------
f = open('reduced/reduced_credits','r')
# omit empty lines and lines containing only whitespace
lines = [line for line in f if line.strip()]
f.close()
lines.sort()

lines = list(set(lines))
for line in lines:
	sentence = line[:-1]
	new_sentence = sentence.upper()
	for i in [0,1]:
		if i == 0:	
			sentence = add_underscore(new_sentence)
		else:
			sentence = new_sentence
		new_line = ""
		s = "<category>"
		new_line = new_line + s + "\n"
		s = "\t" + "<pattern>"+sentence+"</pattern>"
		new_line = new_line + s + "\n"
		s = "\t" + "<template><srai>CREDITS "+COURSECODE+"</srai></template>"
		new_line = new_line + s + "\n"
		s = "</category>"
		new_line = new_line + s + "\n"
		g.write(new_line+"\n")

s = "<!-- answers -->"+"\n"
s = s + "<category>\n"
s = s + "\t"+"<pattern>CREDITS "+COURSECODE+"</pattern>"+"\n"
s = s + "\t<template>\n" + "\t\t<random>\n"
s = s + "\t\t\t<li>$CS "+COURSECODE+" is worth "+CREDITS+" credits. </li>\n"
s = s + "\t\t\t<li>$CS "+COURSECODE+" is of "+CREDITS+" credits. </li>\n"
s = s + "\t\t\t<li>$"+CREDITS+" credits are awarded on successful completion of CS"+COURSECODE+". </li>\n"
s = s + "\t\t\t<li>$"+CREDITS+" credits. </li>\n"
s = s + "\t\t</random>\n" + "\t</template>\n"+"</category>\n"
new_line = s
g.write(new_line+"\n")

#-----------------------------------credits end--------------------------------------------------------

#-------------------------------------syllabus-----------------------------------------------------------
f = open('reduced/reduced_syllabus','r')
# omit empty lines and lines containing only whitespace
lines = [line for line in f if line.strip()]
f.close()
lines.sort()

lines = list(set(lines))
for line in lines:
	sentence = line[:-1]
	new_sentence = sentence.upper()
	for i in [0,1]:
		if i == 0:	
			sentence = add_underscore(new_sentence)
		else:
			sentence = new_sentence
		new_line = ""
		s = "<category>"
		new_line = new_line + s + "\n"
		s = "\t" + "<pattern>"+sentence+"</pattern>"
		new_line = new_line + s + "\n"
		s = "\t" + "<template><srai>SYLLABUS "+COURSECODE+"</srai></template>"
		new_line = new_line + s + "\n"
		s = "</category>"
		new_line = new_line + s + "\n"
		g.write(new_line+"\n")

s = "<!-- answers -->"+"\n"
s = s + "<category>\n"
s = s + "\t"+"<pattern>SYLLABUS "+COURSECODE+"</pattern>"+"\n"
s = s + "\t<template>\n" + "\t\t<random>\n"
s = s + "\t\t\t<li>$The syllabus for CS"+COURSECODE+" is "+SYLLABUS+". </li>\n"
s = s + "\t\t\t<li>$"+SYLLABUS+" is taught in CS"+COURSECODE+". </li>\n"
s = s + "\t\t\t<li>$Prof. "+PROFESSOR+" will teach "+SYLLABUS+" in CS"+COURSECODE+". </li>\n"
s = s + "\t\t\t<li>$"+SYLLABUS+". </li>\n"
s = s + "\t\t</random>\n" + "\t</template>\n"+"</category>\n"
new_line = s
g.write(new_line+"\n")

#-------------------------------------syllabus ends---------------------------------------------------------

#-----------------title-----------------------------------------------------------------------------
f = open('reduced/reduced_title','r')
# omit empty lines and lines containing only whitespace
lines = [line for line in f if line.strip()]
f.close()
lines.sort()

lines = list(set(lines))
for line in lines:
	sentence = line[:-1]
	new_sentence = sentence.upper()
	for i in [0,1]:
		if i == 0:	
			sentence = add_underscore(new_sentence)
		else:
			sentence = new_sentence
		new_line = ""
		s = "<category>"
		new_line = new_line + s + "\n"
		s = "\t" + "<pattern>"+sentence+"</pattern>"
		new_line = new_line + s + "\n"
		s = "\t" + "<template><srai>TITLE "+COURSECODE+"</srai></template>"
		new_line = new_line + s + "\n"
		s = "</category>"
		new_line = new_line + s + "\n"
		g.write(new_line+"\n")

s = "<!-- answers -->"+"\n"
s = s + "<category>\n"
s = s + "\t"+"<pattern>TITLE "+COURSECODE+"</pattern>"+"\n"
s = s + "\t<template>\n" + "\t\t<random>\n"
s = s + "\t\t\t<li>$The course name of CS"+COURSECODE+" is "+TITLE+". </li>\n"
s = s + "\t\t\t<li>$The course title of CS"+COURSECODE+" is "+TITLE+". </li>\n"
s = s + "\t\t\t<li>$Course code CS"+COURSECODE+" is "+TITLE+". </li>\n"
s = s + "\t\t\t<li>$CS"+COURSECODE+" is "+TITLE+". </li>\n"
s = s + "\t\t\t<li>$"+TITLE+". </li>\n"
s = s + "\t\t</random>\n" + "\t</template>\n"+"</category>\n"
new_line = s
g.write(new_line+"\n")

#--------------------title ends--------------------------------------------------------------------------

#---------------------------studentstrength------------------------------------------------------------------
f = open('reduced/reduced_studentstrength','r')
# omit empty lines and lines containing only whitespace
lines = [line for line in f if line.strip()]
f.close()
lines.sort()

lines = list(set(lines))
for line in lines:
	sentence = line[:-1]
	new_sentence = sentence.upper()
	for i in [0,1]:
		if i == 0:	
			sentence = add_underscore(new_sentence)
		else:
			sentence = new_sentence
		new_line = ""
		s = "<category>"
		new_line = new_line + s + "\n"
		s = "\t" + "<pattern>"+sentence+"</pattern>"
		new_line = new_line + s + "\n"
		s = "\t" + "<template><srai>STUDENTSTRENGTH "+COURSECODE+"</srai></template>"
		new_line = new_line + s + "\n"
		s = "</category>"
		new_line = new_line + s + "\n"
		g.write(new_line+"\n")

s = "<!-- answers -->"+"\n"
s = s + "<category>\n"
s = s + "\t"+"<pattern>STUDENTSTRENGTH "+COURSECODE+"</pattern>"+"\n"
s = s + "\t<template>\n" + "\t\t<random>\n"
s = s + "\t\t\t<li>$There are "+STUDENTSTRENGTH+" students in CS"+COURSECODE+". </li>\n"
s = s + "\t\t\t<li>$There are "+STUDENTSTRENGTH+" students in "+TITLE+". </li>\n"
s = s + "\t\t\t<li>$"+STUDENTSTRENGTH+" students are enrolled in CS"+COURSECODE+". </li>\n"
s = s + "\t\t\t<li>$"+STUDENTSTRENGTH+" students are enrolled in "+TITLE+". </li>\n"
s = s + "\t\t\t<li>$"+STUDENTSTRENGTH+" students have signed up for CS"+COURSECODE+". </li>\n"
s = s + "\t\t\t<li>$"+STUDENTSTRENGTH+" students have signed up for "+TITLE+". </li>\n"
s = s + "\t\t\t<li>$The student strength of CS"+COURSECODE+" is "+STUDENTSTRENGTH+". </li>\n"
s = s + "\t\t\t<li>$The student strength of "+TITLE+" is "+STUDENTSTRENGTH+". </li>\n"
s = s + "\t\t</random>\n" + "\t</template>\n"+"</category>\n"
new_line = s
g.write(new_line+"\n")

#-------------------------------------studentstrength done---------------------------------------------------------

#----------------------------------------venue--------------------------------------------------------
f = open('reduced/reduced_venue','r')
# omit empty lines and lines containing only whitespace
lines = [line for line in f if line.strip()]
f.close()
lines.sort()

lines = list(set(lines))
for line in lines:
	sentence = line[:-1]
	new_sentence = sentence.upper()
	for i in [0,1]:
		if i == 0:	
			sentence = add_underscore(new_sentence)
		else:
			sentence = new_sentence
		new_line = ""
		s = "<category>"
		new_line = new_line + s + "\n"
		s = "\t" + "<pattern>"+sentence+"</pattern>"
		new_line = new_line + s + "\n"
		s = "\t" + "<template><srai>VENUE "+COURSECODE+"</srai></template>"
		new_line = new_line + s + "\n"
		s = "</category>"
		new_line = new_line + s + "\n"
		g.write(new_line+"\n")

s = "<!-- answers -->"+"\n"
s = s + "<category>\n"
s = s + "\t"+"<pattern>VENUE "+COURSECODE+"</pattern>"+"\n"
s = s + "\t<template>\n" + "\t\t<random>\n"
s = s + "\t\t\t<li>$The venue is "+VENUE+" and timeslot is "+TIMESLOT+" for CS"+COURSECODE+". </li>\n"
s = s + "\t\t\t<li>$The venue is "+VENUE1+" and timeslot is "+TIMESLOT+" for CS"+COURSECODE+". </li>\n"
s = s + "\t\t\t<li>$The classes are held in "+VENUE+" and timeslot is "+TIMESLOT+" for CS"+COURSECODE+". </li>\n"
s = s + "\t\t\t<li>$The classes are held in "+VENUE1+" and timeslot is "+TIMESLOT+" for CS"+COURSECODE+". </li>\n"
s = s + "\t\t\t<li>$The venue and timeslot are "+VENUE+" and "+TIMESLOT+" respectively for CS"+COURSECODE+". </li>\n"
s = s + "\t\t\t<li>$The venue and timeslot are "+VENUE1+" and "+TIMESLOT+" respectively for CS"+COURSECODE+". </li>\n"
s = s + "\t\t\t<li>$The venue is "+VENUE+", the timeslot is "+TIMESLOT+" for CS"+COURSECODE+". </li>\n"
s = s + "\t\t\t<li>$The venue is "+VENUE1+", the timeslot is "+TIMESLOT+" for CS"+COURSECODE+". </li>\n"
s = s + "\t\t</random>\n" + "\t</template>\n"+"</category>\n"
new_line = s
g.write(new_line+"\n")

#--------------------------------------venue ends--------------------------------------------------------

#------------------------------------------gradeAP------------------------------------------------------
f = open('reduced/reduced_gradeAP','r')
# omit empty lines and lines containing only whitespace
lines = [line for line in f if line.strip()]
f.close()
lines.sort()

lines = list(set(lines))
for line in lines:
	sentence = line[:-1]
	new_sentence = sentence.upper()
	for i in [0,1]:
		if i == 0:	
			sentence = add_underscore(new_sentence)
		else:
			sentence = new_sentence
		new_line = ""
		s = "<category>"
		new_line = new_line + s + "\n"
		s = "\t" + "<pattern>"+sentence+"</pattern>"
		new_line = new_line + s + "\n"
		s = "\t" + "<template><srai>GRADE_AP "+COURSECODE+"</srai></template>"
		new_line = new_line + s + "\n"
		s = "</category>"
		new_line = new_line + s + "\n"
		g.write(new_line+"\n")

s = "<!-- answers -->"+"\n"
s = s + "<category>\n"
s = s + "\t"+"<pattern>GRADE_AP "+COURSECODE+"</pattern>"+"\n"
s = s + "\t<template>\n" + "\t\t<random>\n"
if GRADES[grade_index["AP"]] == "1":
	plural_clause = "student"
else:
	plural_clause = "students"
s = s + "\t\t\t<li>$AP grade for exceptional performance was given to "+GRADES[grade_index["AP"]]+" "+plural_clause+" in CS"+COURSECODE+", 2014. </li>\n"
s = s + "\t\t\t<li>$AP grade for exceptional performance was given to "+GRADES[grade_index["AP"]]+" "+plural_clause+" in "+TITLE+", 2014. </li>\n"
s = s + "\t\t\t<li>$"+GRADES[grade_index["AP"]]+" "+plural_clause+" got AP grade for exceptional performance in CS"+COURSECODE+", 2014. </li>\n"
s = s + "\t\t\t<li>$"+GRADES[grade_index["AP"]]+" "+plural_clause+" got AP grade for exceptional performance in "+TITLE+", 2014. </li>\n"
s = s + "\t\t\t<li>$Number of students getting AP grade was "+GRADES[grade_index["AP"]]+" for exceptional performance in CS"+COURSECODE+", 2014. </li>\n"
s = s + "\t\t\t<li>$Number of students getting AP grade was "+GRADES[grade_index["AP"]]+" for exceptional performance in "+TITLE+", 2014. </li>\n"
s = s + "\t\t\t<li>$"+GRADES[grade_index["AP"]]+". </li>\n"
s = s + "\t\t</random>\n" + "\t</template>\n"+"</category>\n"
new_line = s
g.write(new_line+"\n")

#--------------------------------------------gradeAP ends--------------------------------------------------
#------------------------------------------gradeAA,AB,BB,BC,CC,CD,DD,DX,FR------------------------------------------------------
grade = ""
for count in range(0,9):
	if count == 0:
		grade = "AA"
	if count == 1:
		grade = "AB"
	if count == 2:
		grade = "BB"
	if count == 3:
		grade = "BC"
	if count == 4:
		grade = "CC"
	if count == 5:
		grade = "CD"
	if count == 6:
		grade = "DD"
	if count == 7:
		grade = "DX"
	if count == 8:
		grade = "FR"
	reduced_query_path = "reduced/reduced_grade"+grade
	f = open(reduced_query_path,'r')
	# omit empty lines and lines containing only whitespace
	lines = [line for line in f if line.strip()]
	f.close()
	lines.sort()

	lines = list(set(lines))
	for line in lines:
		sentence = line[:-1]
		new_sentence = sentence.upper()
		for i in [0,1]:
			if i == 0:	
				sentence = add_underscore(new_sentence)
			else:
				sentence = new_sentence
			new_line = ""
			s = "<category>"
			new_line = new_line + s + "\n"
			s = "\t" + "<pattern>"+sentence+"</pattern>"
			new_line = new_line + s + "\n"
			s = "\t" + "<template><srai>GRADE_"+grade+" "+COURSECODE+"</srai></template>"
			new_line = new_line + s + "\n"
			s = "</category>"
			new_line = new_line + s + "\n"
			g.write(new_line+"\n")

	s = "<!-- answers -->"+"\n"
	s = s + "<category>\n"
	s = s + "\t"+"<pattern>GRADE_"+grade+" "+COURSECODE+"</pattern>"+"\n"
	s = s + "\t<template>\n" + "\t\t<random>\n"
	if GRADES[grade_index[grade]] == "1":
		plural_clause = "student"
	else:
		plural_clause = "students"
	s = s + "\t\t\t<li>$"+grade+" grade was given to "+GRADES[grade_index[grade]]+" "+plural_clause+" in CS"+COURSECODE+", 2014. </li>\n"
	s = s + "\t\t\t<li>$"+grade+" grade was given to "+GRADES[grade_index[grade]]+" "+plural_clause+" in "+TITLE+", 2014. </li>\n"
	s = s + "\t\t\t<li>$"+GRADES[grade_index[grade]]+" "+plural_clause+" got "+grade+" grade in CS"+COURSECODE+", 2014. </li>\n"
	s = s + "\t\t\t<li>$"+GRADES[grade_index[grade]]+" "+plural_clause+" got "+grade+" grade in "+TITLE+", 2014. </li>\n"
	s = s + "\t\t\t<li>$Number of students getting "+grade+" grade was "+GRADES[grade_index[grade]]+" in CS"+COURSECODE+", 2014. </li>\n"
	s = s + "\t\t\t<li>$Number of students getting "+grade+" grade was "+GRADES[grade_index[grade]]+" in "+TITLE+", 2014. </li>\n"
	s = s + "\t\t\t<li>$"+GRADES[grade_index[grade]]+". </li>\n"
	s = s + "\t\t</random>\n" + "\t</template>\n"+"</category>\n"
	new_line = s
	g.write(new_line+"\n")
#-------------------------------------------gradeAA,AB,BB,BC,CC,CD,DD,DX,FR ends---------------------------------------------------
#----------------------------------------all grades--------------------------------------------------------
f = open('reduced/reduced_grades','r')
# omit empty lines and lines containing only whitespace
lines = [line for line in f if line.strip()]
f.close()
lines.sort()

lines = list(set(lines))
for line in lines:
	sentence = line[:-1]
	new_sentence = sentence.upper()
	for i in [0,1]:
		if i == 0:	
			sentence = add_underscore(new_sentence)
		else:
			sentence = new_sentence
		new_line = ""
		s = "<category>"
		new_line = new_line + s + "\n"
		s = "\t" + "<pattern>"+sentence+"</pattern>"
		new_line = new_line + s + "\n"
		s = "\t" + "<template><srai>GRADES "+COURSECODE+"</srai></template>"
		new_line = new_line + s + "\n"
		s = "</category>"
		new_line = new_line + s + "\n"
		g.write(new_line+"\n")

s = "<!-- answers -->"+"\n"
s = s + "<category>\n"
s = s + "\t"+"<pattern>GRADES "+COURSECODE+"</pattern>"+"\n"
s = s + "\t<template>\n" + "\t\t<random>\n"
stats = ""
for count in range(0,10):
	if count == 0:
		grade = "AP"
	if count == 1:
		grade = "AA"
	if count == 2:
		grade = "AB"
	if count == 3:
		grade = "BB"
	if count == 4:
		grade = "BC"
	if count == 5:
		grade = "CC"
	if count == 6:
		grade = "CD"
	if count == 7:
		grade = "DD"
	if count == 8:
		grade = "DX"
	if count == 9:
		grade = "FR"
	if count == 9:
		stats = stats+"["+grade+":"+GRADES[grade_index[grade]]+"]"
	else:
		stats = stats+"["+grade+":"+GRADES[grade_index[grade]]+"], "
s = s + "\t\t\t<li>$The grading statistics for CS"+COURSECODE+", 2014 are:- "+stats+". </li>\n"
s = s + "\t\t\t<li>$The grading statistics for "+TITLE+", 2014 are:- "+stats+". </li>\n"
s = s + "\t\t\t<li>$"+stats+". </li>\n"
s = s + "\t\t</random>\n" + "\t</template>\n"+"</category>\n"
new_line = s
g.write(new_line+"\n")

#--------------------------------------all grades ends--------------------------------------------------------
#----------------------------------------references--------------------------------------------------------
f = open('reduced/reduced_references','r')
# omit empty lines and lines containing only whitespace
lines = [line for line in f if line.strip()]
f.close()
lines.sort()

lines = list(set(lines))
for line in lines:
	sentence = line[:-1]
	new_sentence = sentence.upper()
	for i in [0,1]:
		if i == 0:	
			sentence = add_underscore(new_sentence)
		else:
			sentence = new_sentence
		new_line = ""
		s = "<category>"
		new_line = new_line + s + "\n"
		s = "\t" + "<pattern>"+sentence+"</pattern>"
		new_line = new_line + s + "\n"
		s = "\t" + "<template><srai>REFERENCES "+COURSECODE+"</srai></template>"
		new_line = new_line + s + "\n"
		s = "</category>"
		new_line = new_line + s + "\n"
		g.write(new_line+"\n")

s = "<!-- answers -->"+"\n"
s = s + "<category>\n"
s = s + "\t"+"<pattern>REFERENCES "+COURSECODE+"</pattern>"+"\n"
s = s + "\t<template>\n" + "\t\t<random>\n"
s = s + "\t\t\t<li>$The references are "+REFERENCES+" for CS"+COURSECODE+". </li>\n"
s = s + "\t\t\t<li>$The references are "+REFERENCES+" for "+TITLE+". </li>\n"
s = s + "\t\t\t<li>$References according to Professor "+PROFESSOR+" are "+REFERENCES+" for CS"+COURSECODE+". </li>\n"
s = s + "\t\t\t<li>$"+REFERENCES+". </li>\n"
s = s + "\t\t</random>\n" + "\t</template>\n"+"</category>\n"
new_line = s
g.write(new_line+"\n")
#--------------------------------------references ends--------------------------------------------------------
#----------------------------------------type--------------------------------------------------------
f = open('reduced/reduced_type','r')
# omit empty lines and lines containing only whitespace
lines = [line for line in f if line.strip()]
f.close()
lines.sort()

lines = list(set(lines))
for line in lines:
	sentence = line[:-1]
	new_sentence = sentence.upper()
	for i in [0,1]:
		if i == 0:	
			sentence = add_underscore(new_sentence)
		else:
			sentence = new_sentence
		new_line = ""
		s = "<category>"
		new_line = new_line + s + "\n"
		s = "\t" + "<pattern>"+sentence+"</pattern>"
		new_line = new_line + s + "\n"
		s = "\t" + "<template><srai>TYPE "+COURSECODE+"</srai></template>"
		new_line = new_line + s + "\n"
		s = "</category>"
		new_line = new_line + s + "\n"
		g.write(new_line+"\n")

s = "<!-- answers -->"+"\n"
s = s + "<category>\n"
s = s + "\t"+"<pattern>TYPE "+COURSECODE+"</pattern>"+"\n"
s = s + "\t<template>\n" + "\t\t<random>\n"
s = s + "\t\t\t<li>$CS"+COURSECODE+" is a "+TYPE+" course. </li>\n"
s = s + "\t\t\t<li>$It's a "+TYPE+" course "+". </li>\n"
s = s + "\t\t\t<li>$"+TYPE+". </li>\n"
s = s + "\t\t</random>\n" + "\t</template>\n"+"</category>\n"
new_line = s
g.write(new_line+"\n")
#--------------------------------------type ends--------------------------------------------------------
#----------------------------------------duration--------------------------------------------------------
f = open('reduced/reduced_duration','r')
# omit empty lines and lines containing only whitespace
lines = [line for line in f if line.strip()]
f.close()
lines.sort()

lines = list(set(lines))
for line in lines:
	sentence = line[:-1]
	new_sentence = sentence.upper()
	for i in [0,1]:
		if i == 0:	
			sentence = add_underscore(new_sentence)
		else:
			sentence = new_sentence
		new_line = ""
		s = "<category>"
		new_line = new_line + s + "\n"
		s = "\t" + "<pattern>"+sentence+"</pattern>"
		new_line = new_line + s + "\n"
		s = "\t" + "<template><srai>DURATION "+COURSECODE+"</srai></template>"
		new_line = new_line + s + "\n"
		s = "</category>"
		new_line = new_line + s + "\n"
		g.write(new_line+"\n")

s = "<!-- answers -->"+"\n"
s = s + "<category>\n"
s = s + "\t"+"<pattern>DURATION "+COURSECODE+"</pattern>"+"\n"
s = s + "\t<template>\n" + "\t\t<random>\n"
s = s + "\t\t\t<li>$CS"+COURSECODE+" is a "+DURATION+" course. </li>\n"
s = s + "\t\t\t<li>$It's a "+DURATION+" course "+". </li>\n"
s = s + "\t\t\t<li>$CS"+COURSECODE+" is "+DURATION+" long "+". </li>\n"
s = s + "\t\t\t<li>$"+DURATION+". </li>\n"
s = s + "\t\t</random>\n" + "\t</template>\n"+"</category>\n"
new_line = s
g.write(new_line+"\n")
#--------------------------------------duration ends--------------------------------------------------------

#----------------------------------------homepage--------------------------------------------------------
f = open('reduced/reduced_homepage','r')
# omit empty lines and lines containing only whitespace
lines = [line for line in f if line.strip()]
f.close()
lines.sort()

lines = list(set(lines))
for line in lines:
	sentence = line[:-1]
	new_sentence = sentence.upper()
	for i in [0,1]:
		if i == 0:	
			sentence = add_underscore(new_sentence)
		else:
			sentence = new_sentence
		new_line = ""
		s = "<category>"
		new_line = new_line + s + "\n"
		s = "\t" + "<pattern>"+sentence+"</pattern>"
		new_line = new_line + s + "\n"
		s = "\t" + "<template><srai>HOMEPAGE "+COURSECODE+"</srai></template>"
		new_line = new_line + s + "\n"
		s = "</category>"
		new_line = new_line + s + "\n"
		g.write(new_line+"\n")

s = "<!-- answers -->"+"\n"
s = s + "<category>\n"
s = s + "\t"+"<pattern>HOMEPAGE "+COURSECODE+"</pattern>"+"\n"
s = s + "\t<template>\n" + "\t\t<random>\n"
s = s + "\t\t\t<li>$Please visit "+HOMEPAGE+" for more information on CS"+COURSECODE+"</li>\n"
s = s + "\t\t\t<li>$Please visit "+HOMEPAGE+" for more information on "+TITLE+"</li>\n"
s = s + "\t\t\t<li>$The course page is "+HOMEPAGE+". </li>\n"
s = s + "\t\t\t<li>$Course Website is "+HOMEPAGE+". </li>\n"
s = s + "\t\t\t<li>$"+HOMEPAGE+". </li>\n"
s = s + "\t\t</random>\n" + "\t</template>\n"+"</category>\n"
new_line = s
g.write(new_line+"\n")
#--------------------------------------homepage ends--------------------------------------------------------

#----------------------------------------prerequisites--------------------------------------------------------
f = open('reduced/reduced_prerequisites','r')
# omit empty lines and lines containing only whitespace
lines = [line for line in f if line.strip()]
f.close()
lines.sort()

lines = list(set(lines))
for line in lines:
	sentence = line[:-1]
	new_sentence = sentence.upper()
	for i in [0,1]:
		if i == 0:	
			sentence = add_underscore(new_sentence)
		else:
			sentence = new_sentence
		new_line = ""
		s = "<category>"
		new_line = new_line + s + "\n"
		s = "\t" + "<pattern>"+sentence+"</pattern>"
		new_line = new_line + s + "\n"
		s = "\t" + "<template><srai>PREREQUISITES "+COURSECODE+"</srai></template>"
		new_line = new_line + s + "\n"
		s = "</category>"
		new_line = new_line + s + "\n"
		g.write(new_line+"\n")

s = "<!-- answers -->"+"\n"
s = s + "<category>\n"
s = s + "\t"+"<pattern>PREREQUISITES "+COURSECODE+"</pattern>"+"\n"
s = s + "\t<template>\n" + "\t\t<random>\n"
s = s + "\t\t\t<li>$Prerequisites: "+PREREQUISITES+"</li>\n"
s = s + "\t\t\t<li>$You should have completed "+PREREQUISITES+" to register for CS"+COURSECODE+"</li>\n"
s = s + "\t\t\t<li>$You should have completed "+PREREQUISITES+" to register for "+TITLE+"</li>\n"
s = s + "\t\t\t<li>$"+PREREQUISITES+". </li>\n"
s = s + "\t\t</random>\n" + "\t</template>\n"+"</category>\n"
new_line = s
g.write(new_line+"\n")
#--------------------------------------prereq ends--------------------------------------------------------

g.write("</aiml>")
g.close()

