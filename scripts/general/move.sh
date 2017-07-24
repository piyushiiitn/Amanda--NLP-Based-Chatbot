#!/bin/sh
HOME=$(pwd)
cd scripts
#rm -f reduced_*
#python reduction.py
#python create_aiml.py
mv $HOME/scripts/cs344.aiml $HOME/aiml/dept/cs344.aiml
cd ..
