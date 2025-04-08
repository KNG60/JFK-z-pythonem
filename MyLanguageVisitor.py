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


    # Visit a parse tree produced by MyLanguageParser#printStmt.
    def visitPrintStmt(self, ctx:MyLanguageParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#inputStmt.
    def visitInputStmt(self, ctx:MyLanguageParser.InputStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#assignVariableStmt.
    def visitAssignVariableStmt(self, ctx:MyLanguageParser.AssignVariableStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#assignArrayStmt.
    def visitAssignArrayStmt(self, ctx:MyLanguageParser.AssignArrayStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#reassignArrayStmt.
    def visitReassignArrayStmt(self, ctx:MyLanguageParser.ReassignArrayStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#exprStmt.
    def visitExprStmt(self, ctx:MyLanguageParser.ExprStmtContext):
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


    # Visit a parse tree produced by MyLanguageParser#divide.
    def visitDivide(self, ctx:MyLanguageParser.DivideContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#multiply.
    def visitMultiply(self, ctx:MyLanguageParser.MultiplyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#factorExpr.
    def visitFactorExpr(self, ctx:MyLanguageParser.FactorExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#intNumber.
    def visitIntNumber(self, ctx:MyLanguageParser.IntNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#floatNumber.
    def visitFloatNumber(self, ctx:MyLanguageParser.FloatNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#string.
    def visitString(self, ctx:MyLanguageParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#variable.
    def visitVariable(self, ctx:MyLanguageParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#arrayAccess.
    def visitArrayAccess(self, ctx:MyLanguageParser.ArrayAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#bracket.
    def visitBracket(self, ctx:MyLanguageParser.BracketContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#arrayExpr.
    def visitArrayExpr(self, ctx:MyLanguageParser.ArrayExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#exprList.
    def visitExprList(self, ctx:MyLanguageParser.ExprListContext):
        return self.visitChildren(ctx)



del MyLanguageParser