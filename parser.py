import argparse
import sys

def main():
    parser = argparse.ArgumentParser()
    #Recoje datos de la terminal, entrada
    #Tipo obj
    parser.add_argument('--x', type=float,default=1.0,help='Elige el primer numero')
    parser.add_argument('--y', type=float,default=1.0,help='Elige el primer numero')
    parser.add_argument('--operation' , type=str, default='add' ,help='Elige el primer numero')


    #Se añade argumento, se define
    args=parser.parse_args()
    sys.stdout.write(str(calc(args)))

def calc(args):

	if args.operation == 'add':
		resultado = args.x+args.y
	if args.operation == 'div':
		resultado = args.x/args.y
	if args.operation == 'mul':
		resultado = args.x*args.y
	if args.operation == 'res':
		resultado = args.x-args.y
	return resultado


if __name__=='__main__':
	main()