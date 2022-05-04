#/bin/bash
# if not enough args displayed, display an error and die
[ $# -eq 0 ] && echo "Usage: $0 <filename>" && exit

while read SECRET VALUE; 
do 
	NEW_VALUE=`echo $VALUE | base64`; 
	echo $SECRET $NEW_VALUE; 
done < $1
