#!/bin/bash

#messages

function usage(){
	cat << EndOfMessage
usage: dataConverter [-h]

Script that converts data read from different formats to a different format. The formats include JSON, YAML and MongoDB table.

optional arguments:
	-f, --format FORMAT Input format, one of (json, yaml, mongo). If not specified, json is used as a default
	-g, --output format FORMAT Output format, one of (json, yaml, mongo). If not specified, yaml is used as a default
	-i, --input INPUT Input file. When not specified, the stantard input is used
	-o, --output OUTPUT Output file. When not specified, the stantard output is used
 	-h, --help            show this help message and exit

EndOfMessage

}

function gerror(){

message=$*
cat << EndOfMessage
dataConverter: dataConverter [-h]

error: $message
EndOfMessage
}
arguments=( )

inputFormat=json

outputFormat=yaml

while [[ $# -gt 0 ]]
do
	arg=$1
	#echo $arg
	if [ "${arg:0:1}" == "-" ] ; then
		case $arg in

		-h|--help)
			usage
			exit 0
		;;

		-fjson)
		inputFormat=json
		;;

		-fyaml)
		inputFormat=yaml
		;;

		-fmongo)
		inputFormat=mongo
		;;

		-gjson)
		outputFormat=json
		;;

		-gyaml)
		outputFormat=yaml
		;;

	 	-gmongo)
	 	outputFormat=mongo
	 	;;

	 	-i)
	 	input=$2
	 	if [ "$2" == "" ]; then
	 		gerror "Missing argument value"
	 		exit 1
	 	fi
	 	shift
	 	;;

		-o)
	 	output=$2
	 	if [ "$2" == "" ]; then
	 		gerror "Missing argument value"
	 		exit 1
	 	fi
	 	shift
	 	;;

		*)
			gerror "choice" $arg
			exit 1
		;;

		esac
	else
		arguments+=("$arg")
	fi

	shift
done

if [ ${#arguments[@]} -ne 0 ] ; then
	gerror "Too many arguments"
	exit 1
fi

echo "Input format=" $inputFormat
echo "Output format=" $outputFormat
echo "Input=" $input
echo "Output=" $output
exit

