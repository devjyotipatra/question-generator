import logging
import argparse
import sys

from helpers.cli_helpers import *

class Cli(object):

    @classmethod
    def parse(cls):
        parser = argparse.ArgumentParser(description="Birbal Question Generator", add_help=False)
        sub_parsers = parser.add_subparsers()

        topic_parser = sub_parsers.add_parser("topics", help="Keywords that represents the topic")
        topic_parser.add_argument("-k", "--keywords", help="Comma separated list of keywords [max 3]")
        topic_parser.set_defaults(func=cls.get_topics)

        question_parser = sub_parsers.add_parser("questions", help="Questions from the tags")
        question_parser.add_argument("-k", "--tags", help="Comma separated list of tags  \
                                                [returns max 1000 questions for each tag]")
        question_parser.set_defaults(func=cls.get_questions)

        args = parser.parse_args()

        return args


    @classmethod
    def get_topics(cls):
        pass


    @classmethod
    def get_questions(cls):
        pass



def main():
    root = logging.getLogger()
    root.setLevel(logging.INFO)

    ch = logging.StreamHandler(sys.stderr)
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(module)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    root.addHandler(ch)

    Cli.parse()

    sys.exit(0)
