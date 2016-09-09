#!/usr/bin/env python
# Last edit by Daniel Standage, 2016-08-31.
# Last edit by Volker Brendel, 2016-09-06.

from __future__ import print_function
import argparse
import random
import sys
import yaml

class Question(object):
    def __init__(self, data):
        self.data = data
        self.followups = list()

        assert str(data['id']).count('.') <= 1
        self.base_id = str(data['id']).split('.')[0]

    @property
    def followup(self):
        return self.data['type'] == 'continuing'

    @property
    def is_multi_part(self):
        return len(self.followups) > 0

    def add_follow_up(self, question):
        self.followups.append(question)

    def printout(self, qnum, outstream, answer=False):
        key = 'prompt'
        if answer:
            key = 'answer'

        spacer = '. '
        if self.is_multi_part:
            spacer = '. \n'
            text = '    ' + chr(ord('a')) + '. '
            # .replace adds indentation
            text += self.data[key].replace('\n', '\n       ')
            # .rstrip strips extra terminal whitespace
            text = text.rstrip() + '\n\n'
            for i, fu in enumerate(self.followups):
                text += '    ' + chr(ord('a')+ i+1) + '. '
                text += fu.data[key].replace('\n', '\n       ')
                text = text.rstrip() + '\n\n'
        else:
            if qnum < 10:
                text = self.data[key].replace('\n', '\n   ').rstrip() + '\n'
            elif qnum < 100:
                text = self.data[key].replace('\n', '\n    ').rstrip() + '\n'
            else:
                text = self.data[key].replace('\n', '\n     ').rstrip() + '\n'

        print(qnum, spacer, text, sep='', file=outstream)


desc = 'Generate a quiz from the provided question library'
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('--lib', type=argparse.FileType('r'), metavar='FILE',
                    default='../data/FMABqlib.yml', help='question library '
                    'file (default: "../data/FMABqlib.yml")')
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

basequestions = dict()

allquestions = yaml.load(args.lib)
questions = list()
for q in allquestions:
    qst = Question(q)
    if qst.followup:
        parent = basequestions[qst.base_id]
        parent.add_follow_up(qst)
    else:
        basequestions[qst.base_id] = qst;
        questions.append(qst)

if args.sub:
    questions = [q for q in questions if q.data['subject'] == args.sub]
if args.subsub:
    questions = [q for q in questions if q.data['subsubject'] == args.subsub]
if args.type:
    questions = [q for q in questions if q.data['type'] == args.type]
if args.diff:
    questions = [q for q in questions if q.data['difficulty'] == args.diff]
if args.rand > 0:
    questions = random.sample(questions, args.rand)

for i, question in enumerate(questions):
    question.printout(i + 1, args.out)
    if args.answers:
        question.printout(i+1, args.answers, answer=True)
