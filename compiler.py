import sys

from antlr4 import *
from ASTVisitor import ASTVisitor
from llvmlite import binding, ir
from MyLanguageLexer import MyLanguageLexer
from MyLanguageParser import MyLanguageParser


def parse_input(input_file):
    input_stream = FileStream(input_file)
    lexer = MyLanguageLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MyLanguageParser(stream)
    tree = parser.program()
    return tree

def generate_ir(ast):
    module = ir.Module(name="my_module")
    func_type = ir.FunctionType(ir.IntType(32), [], False)
    function = ir.Function(module, func_type, name="main")
    block = function.append_basic_block(name="entry")
    builder = ir.IRBuilder(block)

    visitor = ASTVisitor()
    result = visitor.visit(ast)  # Pobieramy wartość z AST

    int_type = ir.IntType(32)
    value = ir.Constant(int_type, result)  # Tworzymy wartość jako stałą LLVM

    builder.ret(value)  # Zwracamy wartość jako wynik funkcji

    return module

if __name__ == "__main__":
    tree = parse_input("input.txt")  # Wczytanie kodu źródłowego
    llvm_ir = generate_ir(tree)  # Generowanie LLVM IR
    print(llvm_ir)  # Wyświetlenie kodu LLVM
