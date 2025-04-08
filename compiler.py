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
    tree = parse_input("input.txt")
    visitor = ASTVisitor()
    visitor.visit(tree)  # Process AST
