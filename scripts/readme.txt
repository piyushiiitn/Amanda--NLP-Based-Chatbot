Following is the control flow of scripts:

1] python reduction.py:
	raw_query -> reduced_query
2] python create_aiml.py:
	reduced_query -> cs344.aiml
3] ./generate_shell.py
	write the template_course.txt
4] Copy template_course.txt and paste below a line in replace.sh which says :-
		"#--------------paste template data below here-----------------"

5] Run ./replace.sh

Note: replace.py is just a helping script used by replace.sh, 
it is just changing headers of course.aiml files
