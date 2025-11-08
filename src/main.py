import argparse
from rich.console import Console

CONSOLE = Console(color_system="auto")


def insult():
    """A CLI tool that insults you, if insulting yourself isn't enough"""
    a = argparse.ArgumentParser()
    a.add_argument("me", action="store_true", required=False)
    a.add_argument("-insult", action="store_true", required=False)
    a.add_argument("--path", action="store_const", required=False)
    a.add_argument("myself", action="store_true", required=False)
    a.add_argument("-compliment", action="store_true", required=False)
    a.add_argument("--help", action="store_true", required=False)
    a.parse_args()
    pass
