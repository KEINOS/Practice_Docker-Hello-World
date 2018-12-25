#!/usr/bin/env python
import argparse

about  = 'This script prints "Hello World" or given string as an argument.'
parser = argparse.ArgumentParser(about)

parser.add_argument(
    '-e', '--echo',
    help='Echoes the string followed.')

parser.add_argument(
    '-s', '--say',
    help='Returns \'Hello World\'.',
    action='store_true')

args = parser.parse_args()

if args.echo:
    print(args.echo)
else:
    print('Hello World')
