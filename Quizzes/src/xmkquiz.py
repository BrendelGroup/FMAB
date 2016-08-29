#!/usr/bin/env python
# Last edited by Volker Brendel, 2016-08-29.
# Last edited by Daniel Standage, 2016-08-29.

from __future__ import print_function
import argparse
import random
import sys
import yaml

desc = 'Generate a quiz from the provided question library'
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('--lib', type=argparse.FileType('r'), metavar='FILE',
                    default='../data/FMABqlib.yml', help='question library file (default: '
                    '"../data/FMABqlib.yml")')
parser.add_argument('--out', type=argparse.FileType('w'), metavar='FILE',
                    default=sys.stdout, help='output file (default: stdout)')
parser.add_argument('--answers', type=argparse.FileType('w'), metavar='FILE',
                    default=None, help='write answers to specified file')
parser.add_argument('--sub', metavar='W', help='filter by subject')
parser.add_argument('--subsub', metavar='X', help='filter by sub-subject')
parser.add_argument('--type', metavar='Y', help='filter by question type')
parser.add_argument('--diff', metavar='Z', help='filter by difficulty')
parser.add_argument('--rand', metavar='N', type=int, default=0,
                    help='select a random sample of N questions matching the '
                    'specified filtering criteria')
args = parser.parse_args()

questions = yaml.load(args.lib)
if args.sub:
    questions = [q for q in questions if q['subject'] == args.sub]
if args.subsub:
    questions = [q for q in questions if q['subsubject'] == args.subsub]
if args.type:
    questions = [q for q in questions if q['type'] == args.type]
if args.diff:
    questions = [q for q in questions if q['difficulty'] == args.diff]
if args.rand > 0:
    questions = random.sample(questions, args.rand)

for i, q in enumerate(questions):
    qnum = '{:d}. '.format(i + 1)
    prompt = qnum + q['prompt'].replace('\n', '\n   ')  # indentation
    print(prompt, file=args.out)
    if args.answers:
        answer = qnum + q['answer'].replace('\n', '\n   ')
        print(answer, file=args.answers)
