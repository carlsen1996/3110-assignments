#!/bin/bash




move () {
	src="$1"
	dst="$2"

	if [ $# != 2 ]; then
		echo "You need two parameters. You have $#"
		exit 1
	fi

	if [[ -d "$src" && -d "$dst" ]]; then
		mv $src/* $dst
	else
		echo "One of the directories does not exist"
	fi
}

move $1 $2
