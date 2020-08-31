#!/bin/bash


track () {
	mkdir -p $HOME/trackLog
	touch -c $HOME/trackLog/.logFile $HOME/trackLog/.logDiff
	LOGFILE="$HOME/trackLog/.logFile"
	LOGDIFF="$HOME/trackLog/.logDiff"


	if [ $1 == "start" ]; then
		if [[ $(tail -1 ${LOGFILE}) == *"LABEL"* ]]; then
			echo "You can only have one timer running."
			echo "Use track stop to stop the current timer."
		else
			label="$2"
			start="$(date +%s)"
			echo "START " $(date) >> ${LOGFILE}
			echo "LABEL This is $2" >> ${LOGFILE}
		fi
		
	elif [ $1 == "stop" ]; then
		if [[ $(tail -2 ${LOGFILE}) == *"END"* ]]; then
			echo "You have to start a timer to be able to stop it"
			echo "Use track start [label] to start one"
		else
			stop="$(date +%s)"
			diff="$((stop - start))"
			echo "$label $(TZ=UTC0 printf '%(%H:%M:%S)T\n' $diff)" >> ${LOGDIFF}
			echo "END " $(date) >> ${LOGFILE}
			echo "" >> ${LOGFILE}  ##to make a newline between the tasks
		fi

	elif [ $1 == "status" ]; then
		if [[ $(tail -2 ${LOGFILE}) == *"END"* ]]; then
			echo "You dont have an active task"
		else
			echo "The current task is: $label"
		fi
	elif [ $1 == "log" ]; then

		cat ${LOGDIFF}

	else
		echo "track [OPTION]... [label]..."
		echo "avilable options 'start, stop, status'"
		echo "label is the name of the task you want to make"
	fi






}


if [ $# == 2 ]; then
	track $1 $2
elif [ $# == 1 ]; then
	track $1
else
	echo "track [OPTION]... [label]..."
	echo "avilable options 'start, stop, status'"
	echo "label is the name of the task you want to make"
fi
