#!/bin/bash

echo "Bash version.... ${BASH_VERSION}...";


for i in {10..16} 
do
	wget https://people.bath.ac.uk/masrjb/CourseNotes/Notes.bpo/CM30078/slides$i.pdf
done

