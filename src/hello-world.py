#!/usr/bin/env python
import argparse

# Help msg of the app
about  = 'This script prints "Hello World" or given string from the argument.'

# Create arg parser
parser = argparse.ArgumentParser(about)

# Needs 2nd arg
parser.add_argument(
    '-e', '--echo',
    help='Echoes the string followed.')

# Only 1st as a flag
parser.add_argument(
    '-s', '--say',
    help='Returns \'Hello World\'.',
    action='store_true')

# Fetch arguments
args = parser.parse_args()

# Echo the 2nd arg or else just say hello
if args.echo:
    print(args.echo)
else:
    print('Hello World')
