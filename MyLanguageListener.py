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


    # Enter a parse tree produced by MyLanguageParser#ifElseStmt.
    def enterIfElseStmt(self, ctx:MyLanguageParser.IfElseStmtContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#ifElseStmt.
    def exitIfElseStmt(self, ctx:MyLanguageParser.IfElseStmtContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#forStmt.
    def enterForStmt(self, ctx:MyLanguageParser.ForStmtContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#forStmt.
    def exitForStmt(self, ctx:MyLanguageParser.ForStmtContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#functionDeclStmt.
    def enterFunctionDeclStmt(self, ctx:MyLanguageParser.FunctionDeclStmtContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#functionDeclStmt.
    def exitFunctionDeclStmt(self, ctx:MyLanguageParser.FunctionDeclStmtContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#structureDeclStmt.
    def enterStructureDeclStmt(self, ctx:MyLanguageParser.StructureDeclStmtContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#structureDeclStmt.
    def exitStructureDeclStmt(self, ctx:MyLanguageParser.StructureDeclStmtContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#classDeclStmt.
    def enterClassDeclStmt(self, ctx:MyLanguageParser.ClassDeclStmtContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#classDeclStmt.
    def exitClassDeclStmt(self, ctx:MyLanguageParser.ClassDeclStmtContext):
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


    # Enter a parse tree produced by MyLanguageParser#assignArrayStmt.
    def enterAssignArrayStmt(self, ctx:MyLanguageParser.AssignArrayStmtContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#assignArrayStmt.
    def exitAssignArrayStmt(self, ctx:MyLanguageParser.AssignArrayStmtContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#reassignArrayStmt.
    def enterReassignArrayStmt(self, ctx:MyLanguageParser.ReassignArrayStmtContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#reassignArrayStmt.
    def exitReassignArrayStmt(self, ctx:MyLanguageParser.ReassignArrayStmtContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#structInstantiation.
    def enterStructInstantiation(self, ctx:MyLanguageParser.StructInstantiationContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#structInstantiation.
    def exitStructInstantiation(self, ctx:MyLanguageParser.StructInstantiationContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#structFieldAssign.
    def enterStructFieldAssign(self, ctx:MyLanguageParser.StructFieldAssignContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#structFieldAssign.
    def exitStructFieldAssign(self, ctx:MyLanguageParser.StructFieldAssignContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#returnStmt.
    def enterReturnStmt(self, ctx:MyLanguageParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#returnStmt.
    def exitReturnStmt(self, ctx:MyLanguageParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#exprStmt.
    def enterExprStmt(self, ctx:MyLanguageParser.ExprStmtContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#exprStmt.
    def exitExprStmt(self, ctx:MyLanguageParser.ExprStmtContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#ifstatment.
    def enterIfstatment(self, ctx:MyLanguageParser.IfstatmentContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#ifstatment.
    def exitIfstatment(self, ctx:MyLanguageParser.IfstatmentContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#forstatment.
    def enterForstatment(self, ctx:MyLanguageParser.ForstatmentContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#forstatment.
    def exitForstatment(self, ctx:MyLanguageParser.ForstatmentContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#functionDecl.
    def enterFunctionDecl(self, ctx:MyLanguageParser.FunctionDeclContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#functionDecl.
    def exitFunctionDecl(self, ctx:MyLanguageParser.FunctionDeclContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#structureDecl.
    def enterStructureDecl(self, ctx:MyLanguageParser.StructureDeclContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#structureDecl.
    def exitStructureDecl(self, ctx:MyLanguageParser.StructureDeclContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#structField.
    def enterStructField(self, ctx:MyLanguageParser.StructFieldContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#structField.
    def exitStructField(self, ctx:MyLanguageParser.StructFieldContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#type.
    def enterType(self, ctx:MyLanguageParser.TypeContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#type.
    def exitType(self, ctx:MyLanguageParser.TypeContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#paramList.
    def enterParamList(self, ctx:MyLanguageParser.ParamListContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#paramList.
    def exitParamList(self, ctx:MyLanguageParser.ParamListContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#add.
    def enterAdd(self, ctx:MyLanguageParser.AddContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#add.
    def exitAdd(self, ctx:MyLanguageParser.AddContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#equal.
    def enterEqual(self, ctx:MyLanguageParser.EqualContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#equal.
    def exitEqual(self, ctx:MyLanguageParser.EqualContext):
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


    # Enter a parse tree produced by MyLanguageParser#lessThan.
    def enterLessThan(self, ctx:MyLanguageParser.LessThanContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#lessThan.
    def exitLessThan(self, ctx:MyLanguageParser.LessThanContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#notEqual.
    def enterNotEqual(self, ctx:MyLanguageParser.NotEqualContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#notEqual.
    def exitNotEqual(self, ctx:MyLanguageParser.NotEqualContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#greaterEqual.
    def enterGreaterEqual(self, ctx:MyLanguageParser.GreaterEqualContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#greaterEqual.
    def exitGreaterEqual(self, ctx:MyLanguageParser.GreaterEqualContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#lessEqual.
    def enterLessEqual(self, ctx:MyLanguageParser.LessEqualContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#lessEqual.
    def exitLessEqual(self, ctx:MyLanguageParser.LessEqualContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#greaterThan.
    def enterGreaterThan(self, ctx:MyLanguageParser.GreaterThanContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#greaterThan.
    def exitGreaterThan(self, ctx:MyLanguageParser.GreaterThanContext):
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


    # Enter a parse tree produced by MyLanguageParser#arrayAccess.
    def enterArrayAccess(self, ctx:MyLanguageParser.ArrayAccessContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#arrayAccess.
    def exitArrayAccess(self, ctx:MyLanguageParser.ArrayAccessContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#functionCall.
    def enterFunctionCall(self, ctx:MyLanguageParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#functionCall.
    def exitFunctionCall(self, ctx:MyLanguageParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#methodCall.
    def enterMethodCall(self, ctx:MyLanguageParser.MethodCallContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#methodCall.
    def exitMethodCall(self, ctx:MyLanguageParser.MethodCallContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#structAccess.
    def enterStructAccess(self, ctx:MyLanguageParser.StructAccessContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#structAccess.
    def exitStructAccess(self, ctx:MyLanguageParser.StructAccessContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#arrayLiteral.
    def enterArrayLiteral(self, ctx:MyLanguageParser.ArrayLiteralContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#arrayLiteral.
    def exitArrayLiteral(self, ctx:MyLanguageParser.ArrayLiteralContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#bracket.
    def enterBracket(self, ctx:MyLanguageParser.BracketContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#bracket.
    def exitBracket(self, ctx:MyLanguageParser.BracketContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#arrayExpr.
    def enterArrayExpr(self, ctx:MyLanguageParser.ArrayExprContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#arrayExpr.
    def exitArrayExpr(self, ctx:MyLanguageParser.ArrayExprContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#exprList.
    def enterExprList(self, ctx:MyLanguageParser.ExprListContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#exprList.
    def exitExprList(self, ctx:MyLanguageParser.ExprListContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#classDecl.
    def enterClassDecl(self, ctx:MyLanguageParser.ClassDeclContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#classDecl.
    def exitClassDecl(self, ctx:MyLanguageParser.ClassDeclContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#classField.
    def enterClassField(self, ctx:MyLanguageParser.ClassFieldContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#classField.
    def exitClassField(self, ctx:MyLanguageParser.ClassFieldContext):
        pass


    # Enter a parse tree produced by MyLanguageParser#classMethod.
    def enterClassMethod(self, ctx:MyLanguageParser.ClassMethodContext):
        pass

    # Exit a parse tree produced by MyLanguageParser#classMethod.
    def exitClassMethod(self, ctx:MyLanguageParser.ClassMethodContext):
        pass



del MyLanguageParser