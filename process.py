#!/usr/bin/env python

import re
import sys

def main():
    TITLE=False
    DIFFICULTY=False
    LANG=None
    TAGS=False
    line=True
    with sys.stdin as f:
        while line:
            line = f.readline().replace(r'\subsection{', r'\subsection*{').replace(r'\begin{verbatim}', r'\begin{lstlisting}').replace(r'\end{verbatim}', r'\end{lstlisting}')
            if line.startswith('\section{Tags}'):
                TAGS=True
                continue
            if TAGS and len(line.strip()) > 0:
                print '\n'.join(map(lambda x: r'\index{%s}' % x, map(str.strip, line.split(','))))
                TAGS=False
                continue
            if line == r'\\documentclass[]{article}':
                continue
            if line.startswith('\section{Title}'):
                TITLE=True
                continue
            if TITLE and len(line.strip()) > 0:
                print '\chapter{%s}' % line.strip()
                TITLE=False
                continue
            if line.startswith('\section{'):
                print line.replace('\section', '\section*')
                continue
            print line,

if __name__ == '__main__':
    main()
