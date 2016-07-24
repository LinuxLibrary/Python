#!/bin/bash

#OPTIONS="A B C"
for i in A B C
do
	case $i in
	A)
		echo 'A'
	;;
	B)
		echo 'B'
	;;
	C)
		echo 'C'
	;;
	*)
		echo 'Bye'
	;;
	esac
done
