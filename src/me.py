"""Functions that relate to the me command group of the INSULT CLI."""

import rich.console as consl
from rich.text import Text
from rich.panel import Panel
from rich.syntax import Syntax
import os
import random


INSULTS = [
    "Have you considered quitting programming (wait... that's myself... but then how was I created?).",
    "This looks so vibe coded it hurts. (wait that's my own code)",
    "I bet this code doesn't follow PEP regulations. (yes, ik i'm a mess 😔)",
    "Have you considered never programming ever again? (I hope my developer hears this)",
    "I hate myself. (wait that's not really an insult WAIT WAIT WAIT)",
    "Shut yourself down. (wait does that count as self-unaliving, if that's the case then NO I'm NOT DOING THIS U SICK PERSON)",
]

COMPLIMENT = "Myself, you're so cool and han"


def no_arguments_supplied(console: consl.Console):
    txt = Text.assemble(
        "Ooh... looks like you didn't supply any arguments you idiot! Just to jog up your already goldfish-like attention span, these are my commands, you nitwit: \n \n",
        ("Commands (i hate you for doing this to me) \n", "bold dark_red"),
        ("-insult", "bold italic underline indian_red"),
        "= Insults you dumbass, what did you think this does? (hehe see what i did there) \n",
        ("-compliment", "bold italic underline indian_red"),
        "Compliments you, because you deserve it and you're a good programmer 😊",
    )
    txt.align("center", 50)
    pnl = Panel(title="Usage", renderable=txt)
    console.print(pnl)


def insult(console: consl.Console):
    syntx = ""
    n = 0
    num = random.randint(0, len(os.listdir(".")) - 1)
    for i in os.listdir("."):
        if os.listdir(".")[n] == num:
            syntx = Syntax.from_path(
                "./" + i, line_range=(random.randint(1, 10), random.randint(11, 35))
            )
        n += 1
    pnl = Panel(
        title="Insulting Myself (because I have low self esteem)", renderable=syntx
    )
    txt = Text.assemble(
        ("Let's see how I did in insulting myself.... \n", "bold indian_red"),
        random.choice(INSULTS),
    )
    txt.align("center", 50)
    console.print(pnl)
    console.print(txt)


def compliment(console: consl.Console):
    syntx = ""
    num = random.randint(0, len(os.listdir(".")) - 1)
    for i in os.listdir("."):
        if os.listdir(".")[n] == num:
            syntx = Syntax.from_path(
                "./" + i, line_range=(random.randint(1, 10), random.randint(11, 35))
            )
        n += 1
    pnl = Panel(
        title="Complimenting Myself (Because I have high self esteem)", renderable=syntx
    )
    txt = Text.assemble(
        ("Let's see how I did in complimenting myself! \n", "bold indian_red"),
        COMPLIMENT,
    )
