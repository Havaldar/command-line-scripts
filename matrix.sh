#!/bin/bash 

cols=`tput cols`
while true; 
	do
		out=''
		for i in {1..$cols}
			do
				rand=`jot -r 1 0 9`
				out=$out$rand
		done
		printf $out			
done
