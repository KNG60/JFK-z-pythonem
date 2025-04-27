import os
import sys

from antlr4 import *
from llvmlite import binding, ir

from ASTVisitor import ASTVisitor
from MyLanguageLexer import MyLanguageLexer
from MyLanguageParser import MyLanguageParser


def parse_input(input_file):
    input_stream = FileStream(input_file)
    lexer = MyLanguageLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MyLanguageParser(stream)
    return parser.program()  # Returns parse tree

if __name__ == "__main__":
    #Read input code file
    if len(sys.argv) < 2:
        print("compiler <input file>")
        sys.exit(1)
    plik = sys.argv[1]
    try:
        tree = parse_input(plik)
    except Exception as e:
        print(f"Failed to parse program: {str(e)}")
    visitor = ASTVisitor()
    try:
        visitor.visit(tree)  # Process AST
    except Exception as e:
        print(f"Failed to run program: {str(e)}")
    input("\nPress Enter to exit...")
