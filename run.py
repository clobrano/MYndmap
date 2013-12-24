#!/usr/bin/env python

from listparser import *

if __name__ == '__main__':
    ls = ListParser()
    
    notes = [line for line in open('note.txt', 'r')]
    ls.parse(notes)
