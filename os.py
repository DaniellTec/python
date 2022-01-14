import os
import argparse
import sys

#def main():

  #parser = argparse.ArgumentParser()
  #parser.add_argument('--i', type=str, help='--input INPUT Input file. When not specified, the stantard input is used')
  #parser.add_argument('--o', type=str,help='--output OUTPUT Output file. When not specified, the stantard output is used')

  #args=parser.parse_args()
  #sys.stdout.write(str(arguments(args)))

#def arguments(args):

      #fileList = os.listdir(r'C:\Users\eteccar\PycharmProjects\pythonProject')  # open that folder

          #for filename in fileList:

              #if (filename.endswith('.json')):  # check its extension
                 # input = filename.endswith('.json')
                  #print(input)

fileList = os.listdir(r'C:\Users\eteccar\PycharmProjects\pythonProject')  #open that folder
for filename in fileList:
    if(filename.endswith('.json')):  # check its extension
         print(filename)
