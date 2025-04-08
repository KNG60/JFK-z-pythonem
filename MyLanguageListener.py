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


    # Enter a parse tree produced by MyLanguageParser#printStmt.
    def enterPrintStmt(self, ctx:MyLanguageParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#printStmt.
    def exitPrintStmt(self, ctx:MyLanguageParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#inputStmt.
    def enterInputStmt(self, ctx:MyLanguageParser.InputStmtContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#inputStmt.
    def exitInputStmt(self, ctx:MyLanguageParser.InputStmtContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#assignVariableStmt.
    def enterAssignVariableStmt(self, ctx:MyLanguageParser.AssignVariableStmtContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#assignVariableStmt.
    def exitAssignVariableStmt(self, ctx:MyLanguageParser.AssignVariableStmtContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#exprStmt.
    def enterExprStmt(self, ctx:MyLanguageParser.ExprStmtContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#exprStmt.
    def exitExprStmt(self, ctx:MyLanguageParser.ExprStmtContext):
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


    # Enter a parse tree produced by MyLanguageParser#divide.
    def enterDivide(self, ctx:MyLanguageParser.DivideContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#divide.
    def exitDivide(self, ctx:MyLanguageParser.DivideContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#multiply.
    def enterMultiply(self, ctx:MyLanguageParser.MultiplyContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#multiply.
    def exitMultiply(self, ctx:MyLanguageParser.MultiplyContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#factorExpr.
    def enterFactorExpr(self, ctx:MyLanguageParser.FactorExprContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#factorExpr.
    def exitFactorExpr(self, ctx:MyLanguageParser.FactorExprContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#intNumber.
    def enterIntNumber(self, ctx:MyLanguageParser.IntNumberContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#intNumber.
    def exitIntNumber(self, ctx:MyLanguageParser.IntNumberContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#floatNumber.
    def enterFloatNumber(self, ctx:MyLanguageParser.FloatNumberContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#floatNumber.
    def exitFloatNumber(self, ctx:MyLanguageParser.FloatNumberContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#string.
    def enterString(self, ctx:MyLanguageParser.StringContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#string.
    def exitString(self, ctx:MyLanguageParser.StringContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#variable.
    def enterVariable(self, ctx:MyLanguageParser.VariableContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#variable.
    def exitVariable(self, ctx:MyLanguageParser.VariableContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#bracket.
    def enterBracket(self, ctx:MyLanguageParser.BracketContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#bracket.
    def exitBracket(self, ctx:MyLanguageParser.BracketContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#exprList.
    def enterExprList(self, ctx:MyLanguageParser.ExprListContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#exprList.
    def exitExprList(self, ctx:MyLanguageParser.ExprListContext):
        pass



del MyLanguageParser