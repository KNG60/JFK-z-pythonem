import sys

from antlr4 import *

from ASTVisitor import ASTVisitor
from MyLanguageLexer import MyLanguageLexer
from MyLanguageParser import MyLanguageParser

# from llvmlite import binding, ir

def parse_input(input_file):
    input_stream = FileStream(input_file)
    lexer = MyLanguageLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MyLanguageParser(stream)
    return parser.program()  # Returns parse tree

if __name__ == "__main__":
    try:
        tree = parse_input("input.txt")
    except Exception as e:
        print(f"Failed to parse program: {str(e)}")
    visitor = ASTVisitor()
    try:
        visitor.visit(tree)  # Process AST
    except Exception as e:
        print(f"Failed to run program: {str(e)}")
    input("\nPress Enter to exit...")
