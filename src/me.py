"""Functions that relate to the me command group of the INSULT CLI."""

import rich.console as consl
from rich.text import Text
from rich.panel import Panel


def no_arguments_supplied(console: consl.Console):
    txt = Text.assemble(
        "Ooh... looks like you didn't supply any arguments you idiot! Just to jog up your already goldfish-like attention span, these are my commands, you nitwit: \n \n",
        ("Commands (i hate you for doing this to me)", "bold dark_red"),
        ("-insult", "bold italic underline indian_red"),
        "= Insults you dumbass, what did you think this does? (hehe see what i did there)",
        ("-compliment", "bold italic underline indian_red"),
        "Compliments you, because you deserve it and you're a good programmer 😊",
    )
    txt.align("center", 50)
    pnl = Panel(title="Usage", renderable=txt)
    console.print(pnl)
