# Generated from MyLanguage.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,18,106,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,4,0,16,8,0,11,0,12,0,17,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,
        1,44,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,55,8,2,10,2,12,
        2,58,9,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,72,
        8,3,10,3,12,3,75,9,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,3,4,90,8,4,1,5,1,5,3,5,94,8,5,1,5,1,5,1,6,1,6,1,6,5,6,101,
        8,6,10,6,12,6,104,9,6,1,6,0,2,4,6,7,0,2,4,6,8,10,12,0,0,116,0,15,
        1,0,0,0,2,43,1,0,0,0,4,45,1,0,0,0,6,59,1,0,0,0,8,89,1,0,0,0,10,91,
        1,0,0,0,12,97,1,0,0,0,14,16,3,2,1,0,15,14,1,0,0,0,16,17,1,0,0,0,
        17,15,1,0,0,0,17,18,1,0,0,0,18,19,1,0,0,0,19,20,5,0,0,1,20,1,1,0,
        0,0,21,22,5,1,0,0,22,23,5,2,0,0,23,24,3,12,6,0,24,25,5,3,0,0,25,
        44,1,0,0,0,26,27,5,17,0,0,27,28,5,4,0,0,28,44,5,5,0,0,29,30,5,17,
        0,0,30,31,5,4,0,0,31,44,3,4,2,0,32,33,5,17,0,0,33,34,5,4,0,0,34,
        44,3,10,5,0,35,36,5,17,0,0,36,37,5,6,0,0,37,38,3,4,2,0,38,39,5,7,
        0,0,39,40,5,4,0,0,40,41,3,4,2,0,41,44,1,0,0,0,42,44,3,4,2,0,43,21,
        1,0,0,0,43,26,1,0,0,0,43,29,1,0,0,0,43,32,1,0,0,0,43,35,1,0,0,0,
        43,42,1,0,0,0,44,3,1,0,0,0,45,46,6,2,-1,0,46,47,3,6,3,0,47,56,1,
        0,0,0,48,49,10,3,0,0,49,50,5,8,0,0,50,55,3,6,3,0,51,52,10,2,0,0,
        52,53,5,9,0,0,53,55,3,6,3,0,54,48,1,0,0,0,54,51,1,0,0,0,55,58,1,
        0,0,0,56,54,1,0,0,0,56,57,1,0,0,0,57,5,1,0,0,0,58,56,1,0,0,0,59,
        60,6,3,-1,0,60,61,3,8,4,0,61,73,1,0,0,0,62,63,10,4,0,0,63,64,5,10,
        0,0,64,72,3,8,4,0,65,66,10,3,0,0,66,67,5,11,0,0,67,72,3,8,4,0,68,
        69,10,2,0,0,69,70,5,12,0,0,70,72,3,8,4,0,71,62,1,0,0,0,71,65,1,0,
        0,0,71,68,1,0,0,0,72,75,1,0,0,0,73,71,1,0,0,0,73,74,1,0,0,0,74,7,
        1,0,0,0,75,73,1,0,0,0,76,90,5,14,0,0,77,90,5,15,0,0,78,90,5,16,0,
        0,79,90,5,17,0,0,80,81,5,17,0,0,81,82,5,6,0,0,82,83,3,4,2,0,83,84,
        5,7,0,0,84,90,1,0,0,0,85,86,5,2,0,0,86,87,3,4,2,0,87,88,5,3,0,0,
        88,90,1,0,0,0,89,76,1,0,0,0,89,77,1,0,0,0,89,78,1,0,0,0,89,79,1,
        0,0,0,89,80,1,0,0,0,89,85,1,0,0,0,90,9,1,0,0,0,91,93,5,6,0,0,92,
        94,3,12,6,0,93,92,1,0,0,0,93,94,1,0,0,0,94,95,1,0,0,0,95,96,5,7,
        0,0,96,11,1,0,0,0,97,102,3,4,2,0,98,99,5,13,0,0,99,101,3,4,2,0,100,
        98,1,0,0,0,101,104,1,0,0,0,102,100,1,0,0,0,102,103,1,0,0,0,103,13,
        1,0,0,0,104,102,1,0,0,0,9,17,43,54,56,71,73,89,93,102
    ]

class MyLanguageParser ( Parser ):

    grammarFileName = "MyLanguage.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'ctrl_v'", "'('", "')'", "'='", "'ctrl_c'", 
                     "'['", "']'", "'+'", "'-'", "'*'", "'/'", "':'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "INT", "FLOAT", "STRING", 
                      "VARIABLE", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_expr = 2
    RULE_term = 3
    RULE_factor = 4
    RULE_arrayExpr = 5
    RULE_exprList = 6

    ruleNames =  [ "program", "statement", "expr", "term", "factor", "arrayExpr", 
                   "exprList" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    INT=14
    FLOAT=15
    STRING=16
    VARIABLE=17
    WS=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MyLanguageParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLanguageParser.StatementContext)
            else:
                return self.getTypedRuleContext(MyLanguageParser.StatementContext,i)


        def getRuleIndex(self):
            return MyLanguageParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MyLanguageParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.statement()
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 245766) != 0)):
                    break

            self.state = 19
            self.match(MyLanguageParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MyLanguageParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PrintStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLanguageParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def exprList(self):
            return self.getTypedRuleContext(MyLanguageParser.ExprListContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStmt" ):
                listener.enterPrintStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStmt" ):
                listener.exitPrintStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStmt" ):
                return visitor.visitPrintStmt(self)
            else:
                return visitor.visitChildren(self)


    class AssignArrayStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLanguageParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(MyLanguageParser.VARIABLE, 0)
        def arrayExpr(self):
            return self.getTypedRuleContext(MyLanguageParser.ArrayExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignArrayStmt" ):
                listener.enterAssignArrayStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignArrayStmt" ):
                listener.exitAssignArrayStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignArrayStmt" ):
                return visitor.visitAssignArrayStmt(self)
            else:
                return visitor.visitChildren(self)


    class ExprStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLanguageParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MyLanguageParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprStmt" ):
                listener.enterExprStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprStmt" ):
                listener.exitExprStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprStmt" ):
                return visitor.visitExprStmt(self)
            else:
                return visitor.visitChildren(self)


    class AssignVariableStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLanguageParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(MyLanguageParser.VARIABLE, 0)
        def expr(self):
            return self.getTypedRuleContext(MyLanguageParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignVariableStmt" ):
                listener.enterAssignVariableStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignVariableStmt" ):
                listener.exitAssignVariableStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignVariableStmt" ):
                return visitor.visitAssignVariableStmt(self)
            else:
                return visitor.visitChildren(self)


    class ReassignArrayStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLanguageParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(MyLanguageParser.VARIABLE, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLanguageParser.ExprContext)
            else:
                return self.getTypedRuleContext(MyLanguageParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReassignArrayStmt" ):
                listener.enterReassignArrayStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReassignArrayStmt" ):
                listener.exitReassignArrayStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReassignArrayStmt" ):
                return visitor.visitReassignArrayStmt(self)
            else:
                return visitor.visitChildren(self)


    class InputStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLanguageParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(MyLanguageParser.VARIABLE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInputStmt" ):
                listener.enterInputStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInputStmt" ):
                listener.exitInputStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInputStmt" ):
                return visitor.visitInputStmt(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = MyLanguageParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 43
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = MyLanguageParser.PrintStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.match(MyLanguageParser.T__0)
                self.state = 22
                self.match(MyLanguageParser.T__1)
                self.state = 23
                self.exprList()
                self.state = 24
                self.match(MyLanguageParser.T__2)
                pass

            elif la_ == 2:
                localctx = MyLanguageParser.InputStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.match(MyLanguageParser.VARIABLE)
                self.state = 27
                self.match(MyLanguageParser.T__3)
                self.state = 28
                self.match(MyLanguageParser.T__4)
                pass

            elif la_ == 3:
                localctx = MyLanguageParser.AssignVariableStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 29
                self.match(MyLanguageParser.VARIABLE)
                self.state = 30
                self.match(MyLanguageParser.T__3)
                self.state = 31
                self.expr(0)
                pass

            elif la_ == 4:
                localctx = MyLanguageParser.AssignArrayStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 32
                self.match(MyLanguageParser.VARIABLE)
                self.state = 33
                self.match(MyLanguageParser.T__3)
                self.state = 34
                self.arrayExpr()
                pass

            elif la_ == 5:
                localctx = MyLanguageParser.ReassignArrayStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 35
                self.match(MyLanguageParser.VARIABLE)
                self.state = 36
                self.match(MyLanguageParser.T__5)
                self.state = 37
                self.expr(0)
                self.state = 38
                self.match(MyLanguageParser.T__6)
                self.state = 39
                self.match(MyLanguageParser.T__3)
                self.state = 40
                self.expr(0)
                pass

            elif la_ == 6:
                localctx = MyLanguageParser.ExprStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 42
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MyLanguageParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AddContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLanguageParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MyLanguageParser.ExprContext,0)

        def term(self):
            return self.getTypedRuleContext(MyLanguageParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd" ):
                listener.enterAdd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd" ):
                listener.exitAdd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd" ):
                return visitor.visitAdd(self)
            else:
                return visitor.visitChildren(self)


    class TermExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLanguageParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(MyLanguageParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermExpr" ):
                listener.enterTermExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermExpr" ):
                listener.exitTermExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermExpr" ):
                return visitor.visitTermExpr(self)
            else:
                return visitor.visitChildren(self)


    class SubtractContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLanguageParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MyLanguageParser.ExprContext,0)

        def term(self):
            return self.getTypedRuleContext(MyLanguageParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubtract" ):
                listener.enterSubtract(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubtract" ):
                listener.exitSubtract(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubtract" ):
                return visitor.visitSubtract(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MyLanguageParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MyLanguageParser.TermExprContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 46
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 56
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 54
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = MyLanguageParser.AddContext(self, MyLanguageParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 48
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 49
                        self.match(MyLanguageParser.T__7)
                        self.state = 50
                        self.term(0)
                        pass

                    elif la_ == 2:
                        localctx = MyLanguageParser.SubtractContext(self, MyLanguageParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 51
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 52
                        self.match(MyLanguageParser.T__8)
                        self.state = 53
                        self.term(0)
                        pass

             
                self.state = 58
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MyLanguageParser.RULE_term

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class DivideContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLanguageParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(MyLanguageParser.TermContext,0)

        def factor(self):
            return self.getTypedRuleContext(MyLanguageParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivide" ):
                listener.enterDivide(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivide" ):
                listener.exitDivide(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDivide" ):
                return visitor.visitDivide(self)
            else:
                return visitor.visitChildren(self)


    class MultiplyContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLanguageParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(MyLanguageParser.TermContext,0)

        def factor(self):
            return self.getTypedRuleContext(MyLanguageParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiply" ):
                listener.enterMultiply(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiply" ):
                listener.exitMultiply(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiply" ):
                return visitor.visitMultiply(self)
            else:
                return visitor.visitChildren(self)


    class FactorExprContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLanguageParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factor(self):
            return self.getTypedRuleContext(MyLanguageParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactorExpr" ):
                listener.enterFactorExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactorExpr" ):
                listener.exitFactorExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactorExpr" ):
                return visitor.visitFactorExpr(self)
            else:
                return visitor.visitChildren(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MyLanguageParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MyLanguageParser.FactorExprContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 60
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 73
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 71
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = MyLanguageParser.MultiplyContext(self, MyLanguageParser.TermContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 62
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 63
                        self.match(MyLanguageParser.T__9)
                        self.state = 64
                        self.factor()
                        pass

                    elif la_ == 2:
                        localctx = MyLanguageParser.DivideContext(self, MyLanguageParser.TermContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 65
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 66
                        self.match(MyLanguageParser.T__10)
                        self.state = 67
                        self.factor()
                        pass

                    elif la_ == 3:
                        localctx = MyLanguageParser.DivideContext(self, MyLanguageParser.TermContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 68
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 69
                        self.match(MyLanguageParser.T__11)
                        self.state = 70
                        self.factor()
                        pass

             
                self.state = 75
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MyLanguageParser.RULE_factor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class StringContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLanguageParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(MyLanguageParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)


    class VariableContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLanguageParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(MyLanguageParser.VARIABLE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)


    class BracketContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLanguageParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MyLanguageParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBracket" ):
                listener.enterBracket(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBracket" ):
                listener.exitBracket(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBracket" ):
                return visitor.visitBracket(self)
            else:
                return visitor.visitChildren(self)


    class IntNumberContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLanguageParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(MyLanguageParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntNumber" ):
                listener.enterIntNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntNumber" ):
                listener.exitIntNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntNumber" ):
                return visitor.visitIntNumber(self)
            else:
                return visitor.visitChildren(self)


    class ArrayAccessContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLanguageParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(MyLanguageParser.VARIABLE, 0)
        def expr(self):
            return self.getTypedRuleContext(MyLanguageParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayAccess" ):
                listener.enterArrayAccess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayAccess" ):
                listener.exitArrayAccess(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayAccess" ):
                return visitor.visitArrayAccess(self)
            else:
                return visitor.visitChildren(self)


    class FloatNumberContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MyLanguageParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(MyLanguageParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloatNumber" ):
                listener.enterFloatNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloatNumber" ):
                listener.exitFloatNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatNumber" ):
                return visitor.visitFloatNumber(self)
            else:
                return visitor.visitChildren(self)



    def factor(self):

        localctx = MyLanguageParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_factor)
        try:
            self.state = 89
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = MyLanguageParser.IntNumberContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.match(MyLanguageParser.INT)
                pass

            elif la_ == 2:
                localctx = MyLanguageParser.FloatNumberContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self.match(MyLanguageParser.FLOAT)
                pass

            elif la_ == 3:
                localctx = MyLanguageParser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 78
                self.match(MyLanguageParser.STRING)
                pass

            elif la_ == 4:
                localctx = MyLanguageParser.VariableContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 79
                self.match(MyLanguageParser.VARIABLE)
                pass

            elif la_ == 5:
                localctx = MyLanguageParser.ArrayAccessContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 80
                self.match(MyLanguageParser.VARIABLE)
                self.state = 81
                self.match(MyLanguageParser.T__5)
                self.state = 82
                self.expr(0)
                self.state = 83
                self.match(MyLanguageParser.T__6)
                pass

            elif la_ == 6:
                localctx = MyLanguageParser.BracketContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 85
                self.match(MyLanguageParser.T__1)
                self.state = 86
                self.expr(0)
                self.state = 87
                self.match(MyLanguageParser.T__2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprList(self):
            return self.getTypedRuleContext(MyLanguageParser.ExprListContext,0)


        def getRuleIndex(self):
            return MyLanguageParser.RULE_arrayExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayExpr" ):
                listener.enterArrayExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayExpr" ):
                listener.exitArrayExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayExpr" ):
                return visitor.visitArrayExpr(self)
            else:
                return visitor.visitChildren(self)




    def arrayExpr(self):

        localctx = MyLanguageParser.ArrayExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_arrayExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(MyLanguageParser.T__5)
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 245764) != 0):
                self.state = 92
                self.exprList()


            self.state = 95
            self.match(MyLanguageParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyLanguageParser.ExprContext)
            else:
                return self.getTypedRuleContext(MyLanguageParser.ExprContext,i)


        def getRuleIndex(self):
            return MyLanguageParser.RULE_exprList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprList" ):
                listener.enterExprList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprList" ):
                listener.exitExprList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprList" ):
                return visitor.visitExprList(self)
            else:
                return visitor.visitChildren(self)




    def exprList(self):

        localctx = MyLanguageParser.ExprListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_exprList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.expr(0)
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 98
                self.match(MyLanguageParser.T__12)
                self.state = 99
                self.expr(0)
                self.state = 104
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        self._predicates[3] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




