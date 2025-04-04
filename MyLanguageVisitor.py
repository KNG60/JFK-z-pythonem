# Generated from MyLanguage.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MyLanguageParser import MyLanguageParser
else:
    from MyLanguageParser import MyLanguageParser

# This class defines a complete generic visitor for a parse tree produced by MyLanguageParser.

class MyLanguageVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MyLanguageParser#program.
    def visitProgram(self, ctx:MyLanguageParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#statement.
    def visitStatement(self, ctx:MyLanguageParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#add.
    def visitAdd(self, ctx:MyLanguageParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#termExpr.
    def visitTermExpr(self, ctx:MyLanguageParser.TermExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#subtract.
    def visitSubtract(self, ctx:MyLanguageParser.SubtractContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#number.
    def visitNumber(self, ctx:MyLanguageParser.NumberContext):
        return self.visitChildren(ctx)



del MyLanguageParser