# Generated from MyLanguage.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MyLanguageParser import MyLanguageParser
else:
    from MyLanguageParser import MyLanguageParser

# This class defines a complete listener for a parse tree produced by MyLanguageParser.
class MyLanguageListener(ParseTreeListener):

    # Enter a parse tree produced by MyLanguageParser#program.
    def enterProgram(self, ctx:MyLanguageParser.ProgramContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#program.
    def exitProgram(self, ctx:MyLanguageParser.ProgramContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#statement.
    def enterStatement(self, ctx:MyLanguageParser.StatementContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#statement.
    def exitStatement(self, ctx:MyLanguageParser.StatementContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#add.
    def enterAdd(self, ctx:MyLanguageParser.AddContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#add.
    def exitAdd(self, ctx:MyLanguageParser.AddContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#termExpr.
    def enterTermExpr(self, ctx:MyLanguageParser.TermExprContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#termExpr.
    def exitTermExpr(self, ctx:MyLanguageParser.TermExprContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#subtract.
    def enterSubtract(self, ctx:MyLanguageParser.SubtractContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#subtract.
    def exitSubtract(self, ctx:MyLanguageParser.SubtractContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#number.
    def enterNumber(self, ctx:MyLanguageParser.NumberContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#number.
    def exitNumber(self, ctx:MyLanguageParser.NumberContext):
        pass



del MyLanguageParser