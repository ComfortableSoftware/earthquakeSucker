#!/usr/bin/python


import getopt
from sys import argv


OPTSTR = f"""x:yet:"""
OPTS, ARGS = getopt.getopt(argv[1:], OPTSTR)

print(f"""
OPTS
{str(OPTS)}
ARGS
{str(ARGS)}
""")

