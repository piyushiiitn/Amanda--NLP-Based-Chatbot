import sys

g = open('template_course.txt','w')

course_list = ["cs101","cs207","cs213","cs215","cs218","cs224","cs251","cs293","cs317","cs341","cs386","cs387","cs475","cs601","cs606","cs613","cs615","cs616","cs618","cs620","cs631","cs641","cs663","cs675","cs682","cs683","cs684","cs691","cs692","cs721","cs725","cs738","cs740","cs745","cs747"]


#--------------------------------------------------------------
# cd ./reduced/
# sed -i 's/344/305/g' reduced_prof 
# sed -i 's/344/305/g' reduced_title 
# sed -i 's/344/305/g' reduced_credits 
# sed -i 's/344/305/g' reduced_syllabus 
# sed -i 's/344/305/g' reduced_studentstrength 
# sed -i 's/344/305/g' reduced_venue 
# sed -i 's/344/305/g' reduced_gradeAP 
# sed -i 's/344/305/g' reduced_gradeAA 
# sed -i 's/344/305/g' reduced_gradeAB 
# sed -i 's/344/305/g' reduced_gradeBB 
# sed -i 's/344/305/g' reduced_gradeBC 
# sed -i 's/344/305/g' reduced_gradeCC 
# sed -i 's/344/305/g' reduced_gradeCD 
# sed -i 's/344/305/g' reduced_gradeDD 
# sed -i 's/344/305/g' reduced_gradeDX 
# sed -i 's/344/305/g' reduced_gradeFR 
# sed -i 's/344/305/g' reduced_grades
# sed -i 's/344/305/g' reduced_type 
# sed -i 's/344/305/g' reduced_duration 
# sed -i 's/344/305/g' reduced_prerequisites
# sed -i 's/344/305/g' reduced_references
# sed -i 's/344/305/g' reduced_homepage  

# cd ../
# python replace.py ./data/cs305.txt
# python cpy_aiml.py
# rm -f cpy_aiml.py
# mv cs305.aiml ./cs305/
# cp ./cs305/cs305.aiml ../aiml/dept/cs305.aiml

#--------------------------------------------------------------
s = ""
s = s+"#--------------------------------------------------------------\n"
s = s+"cd ./reduced/"+"\n"
s = s+"sed -i 's/344/305/g' reduced_prof"+"\n"
s = s+"sed -i 's/344/305/g' reduced_title"+"\n"
s = s+"sed -i 's/344/305/g' reduced_credits"+"\n"
s = s+"sed -i 's/344/305/g' reduced_syllabus"+"\n"
s = s+"sed -i 's/344/305/g' reduced_studentstrength"+"\n"
s = s+"sed -i 's/344/305/g' reduced_venue"+"\n"
s = s+"sed -i 's/344/305/g' reduced_gradeAP"+"\n"
s = s+"sed -i 's/344/305/g' reduced_gradeAA"+"\n"
s = s+"sed -i 's/344/305/g' reduced_gradeAB"+"\n"
s = s+"sed -i 's/344/305/g' reduced_gradeBB"+"\n"
s = s+"sed -i 's/344/305/g' reduced_gradeBC"+"\n"
s = s+"sed -i 's/344/305/g' reduced_gradeCC"+"\n"
s = s+"sed -i 's/344/305/g' reduced_gradeCD"+"\n"
s = s+"sed -i 's/344/305/g' reduced_gradeDD"+"\n"
s = s+"sed -i 's/344/305/g' reduced_gradeDX"+"\n"
s = s+"sed -i 's/344/305/g' reduced_gradeFR"+"\n"
s = s+"sed -i 's/344/305/g' reduced_grades"+"\n"
s = s+"sed -i 's/344/305/g' reduced_type"+"\n"
s = s+"sed -i 's/344/305/g' reduced_duration"+"\n"
s = s+"sed -i 's/344/305/g' reduced_prerequisites"+"\n"
s = s+"sed -i 's/344/305/g' reduced_references"+"\n"
s = s+"sed -i 's/344/305/g' reduced_homepage"+"\n"
s = s+"\n"
s = s+"cd ../"+"\n"
s = s+"python replace.py ./data/cs305.txt"+"\n"
s = s+"python cpy_aiml.py"+"\n"
s = s+"rm -f cpy_aiml.py"+"\n"
s = s+"mv cs305.aiml ./cs305/"+"\n"
s = s+"cp ./cs305/cs305.aiml ../aiml/dept/cs305.aiml"+"\n"
s = s+"\n"
s = s+"#--------------------------------------------------------------\n"

g.write(s)
prev = "344"
current = "305"

for course in course_list:
	course_num = course[2:]
	s = s.replace(current,course_num)
	s = s.replace(prev,current)
	prev = current
	current = course_num
	g.write(s)
