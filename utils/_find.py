#!/usr/bin/env python3
'''
    the shebang line above will be removed
    as this is not a standalone script.
    File I/O for word search
'''

import argparse

def find_me(self, word):
    '''
        finds a word in a text and
        counts occurences
    '''
    word = word.lower()
    occurences = 0
    lines_found = []

    with open(self, 'r') as f:
        '''
            iterate through the lines to:
                find and
                count occurences
        '''
        for line_number, line in enumerate(f, start=1):
            '''
                Convert lines to lower case
            '''
            line_lower = line.lower()
            if word in line_lower:
                # count occurences
                count_in_line = line_lower.count(word)
                occurences += count_in_line
                # record line number and counts
                lines_found.apped((line_number, count_in_line))
