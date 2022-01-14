import argparse
import sys
import os

def main():

  parser = argparse.ArgumentParser()
  #Calls parse
  parser.add_argument('--f', type=str, default='json', help='--format FORMAT Input format, one of (json, yaml, mongo). If not specified, json is used as a default')
  parser.add_argument('--g', type=str, default='yaml', help='--output format FORMAT Output format, one of (json, yaml, mongo). If not specified, yaml is used as a default')
  parser.add_argument('--i', type=str, help='--input INPUT Input file. When not specified, the stantard input is used')
  parser.add_argument('--o', type=str, help='--output OUTPUT Output file. When not specified, the stantard output is used')
  #parser.add_argument(' ', type=str, help='Invalid choice')
  #List of arguments
  #parser.add_argument('--help', type=str, help=help)

  args=parser.parse_args()
  #parse as argument
  sys.stdout.write(str(arguments(args)))
  #Takes the values of the input terminal

def arguments(args):

  #Variables
  inputFormat = "Input format selected: json"
  outputFormat = " Output format selected: yaml"
  #input = "\ninput file: "
  #output = "\noutput file: "

  #Case
  #if args.f == " ":
    #inputFormat = 'Invalid choice', args
  #Inputs
  if args.f == "json":
    inputFormat = '\nInput format selected: json'
  if args.f == "yaml":
    inputFormat = '\nInput format selected:yaml'
  if args.f == "mongo":
    inputFormat = '\nInput format selected: mongo'

  #Outputs
  if args.g == "json":
    outputFormat = '\nOutput format selected: json'
  if args.g == "yaml":
    outputFormat = '\nOutput format selected: yaml'
  if args.g == "mongo":
    outputFormat = '\nOutput format selected: mongo'

  #Input, Output

  fileList = os.listdir(r'C:\Users\eteccar\PycharmProjects\pythonProject')  # open that folder
  for filename in fileList:
    input = filename
    if args.i == "json":
      if (input.endswith('.json')):  # check its extension
        print(inputFormat, outputFormat, "\nInput file:", input)
       #if args.i == "yaml":
        #if (input.endswith('.yaml')):  # check its extension
          #print(inputFormat, outputFormat, "\nInput file:", input)

  #Return values

  #if args.i == "yaml":
    #fileList = os.listdir(r'C:\Users\eteccar\PycharmProjects\pythonProject')  # open that folder

    #for filename in fileList:

        #if (filename.endswith('.yaml')):  # check its extension

  #Return values

  #print("Input=", input)
  #print("Output=", output)
  #return (inputFormat)
  #return (outputFormat)
  #print (inputFormat, outputFormat)
  #print(inputFormat)
  #print(outputFormat)

if __name__=='__main__':
	main()
    #is used to execute some code only if the file was run directly, and not imported.