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


    # Visit a parse tree produced by MyLanguageParser#ifElseStmt.
    def visitIfElseStmt(self, ctx:MyLanguageParser.IfElseStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#forStmt.
    def visitForStmt(self, ctx:MyLanguageParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#functionDeclStmt.
    def visitFunctionDeclStmt(self, ctx:MyLanguageParser.FunctionDeclStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#structureDeclStmt.
    def visitStructureDeclStmt(self, ctx:MyLanguageParser.StructureDeclStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#classDeclStmt.
    def visitClassDeclStmt(self, ctx:MyLanguageParser.ClassDeclStmtContext):
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


    # Visit a parse tree produced by MyLanguageParser#structInstantiation.
    def visitStructInstantiation(self, ctx:MyLanguageParser.StructInstantiationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#structFieldAssign.
    def visitStructFieldAssign(self, ctx:MyLanguageParser.StructFieldAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#returnStmt.
    def visitReturnStmt(self, ctx:MyLanguageParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#exprStmt.
    def visitExprStmt(self, ctx:MyLanguageParser.ExprStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#ifstatment.
    def visitIfstatment(self, ctx:MyLanguageParser.IfstatmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#forstatment.
    def visitForstatment(self, ctx:MyLanguageParser.ForstatmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#functionDecl.
    def visitFunctionDecl(self, ctx:MyLanguageParser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#structureDecl.
    def visitStructureDecl(self, ctx:MyLanguageParser.StructureDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#structField.
    def visitStructField(self, ctx:MyLanguageParser.StructFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#type.
    def visitType(self, ctx:MyLanguageParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#paramList.
    def visitParamList(self, ctx:MyLanguageParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#add.
    def visitAdd(self, ctx:MyLanguageParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#equal.
    def visitEqual(self, ctx:MyLanguageParser.EqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#termExpr.
    def visitTermExpr(self, ctx:MyLanguageParser.TermExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#subtract.
    def visitSubtract(self, ctx:MyLanguageParser.SubtractContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#lessThan.
    def visitLessThan(self, ctx:MyLanguageParser.LessThanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#notEqual.
    def visitNotEqual(self, ctx:MyLanguageParser.NotEqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#greaterEqual.
    def visitGreaterEqual(self, ctx:MyLanguageParser.GreaterEqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#lessEqual.
    def visitLessEqual(self, ctx:MyLanguageParser.LessEqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#greaterThan.
    def visitGreaterThan(self, ctx:MyLanguageParser.GreaterThanContext):
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


    # Visit a parse tree produced by MyLanguageParser#functionCall.
    def visitFunctionCall(self, ctx:MyLanguageParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#methodCall.
    def visitMethodCall(self, ctx:MyLanguageParser.MethodCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#structAccess.
    def visitStructAccess(self, ctx:MyLanguageParser.StructAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#arrayLiteral.
    def visitArrayLiteral(self, ctx:MyLanguageParser.ArrayLiteralContext):
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


    # Visit a parse tree produced by MyLanguageParser#classDecl.
    def visitClassDecl(self, ctx:MyLanguageParser.ClassDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#classField.
    def visitClassField(self, ctx:MyLanguageParser.ClassFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyLanguageParser#classMethod.
    def visitClassMethod(self, ctx:MyLanguageParser.ClassMethodContext):
        return self.visitChildren(ctx)



del MyLanguageParser