"""
TODO docstring.

Docstring
"""

from argparse import ArgumentParser


class CmdArgs():
    """
    TODO docstring.

    Docstring
    """

    def __init__(self):
        """
        TODO docstring.

        Docstring
        """
        self.parser = ArgumentParser(prog="pdedup",
                                     description="""This program is used to
                                     find and/or remove duplicated files in
                                     given path""")

        self.__cmd_args()

    def __cmd_args(self):
        """
        TODO docstring.

        Docstring
        """
        self.parser.add_argument("--dir-path", "-d", help="""Abosulte/Relative
                                 path to directory. [Detaul: '.']""",
                                 required=True, default=".", type=str,
                                 dest="dir_path")

        self.parser.add_argument("--list-only", "-l", action="store_true",
                                 default=False, required=False,
                                 help="""Don't delete the duplicated files
                                 only list them. [Default: False]""",
                                 dest="list_only")

    @classmethod
    def cmd_parsed_args(cls):
        """
        TODO docstring.

        Docstring
        """
        return cls().parser.parse_args()
