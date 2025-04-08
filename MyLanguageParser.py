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
        4,1,16,83,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,4,
        0,14,8,0,11,0,12,0,15,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,3,1,32,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,
        43,8,2,10,2,12,2,46,9,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,5,3,60,8,3,10,3,12,3,63,9,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,3,4,73,8,4,1,5,1,5,1,5,5,5,78,8,5,10,5,12,5,81,9,5,1,5,0,2,4,
        6,6,0,2,4,6,8,10,0,0,90,0,13,1,0,0,0,2,31,1,0,0,0,4,33,1,0,0,0,6,
        47,1,0,0,0,8,72,1,0,0,0,10,74,1,0,0,0,12,14,3,2,1,0,13,12,1,0,0,
        0,14,15,1,0,0,0,15,13,1,0,0,0,15,16,1,0,0,0,16,17,1,0,0,0,17,18,
        5,0,0,1,18,1,1,0,0,0,19,20,5,1,0,0,20,21,5,2,0,0,21,22,3,10,5,0,
        22,23,5,3,0,0,23,32,1,0,0,0,24,25,5,15,0,0,25,26,5,4,0,0,26,32,5,
        5,0,0,27,28,5,15,0,0,28,29,5,4,0,0,29,32,3,4,2,0,30,32,3,4,2,0,31,
        19,1,0,0,0,31,24,1,0,0,0,31,27,1,0,0,0,31,30,1,0,0,0,32,3,1,0,0,
        0,33,34,6,2,-1,0,34,35,3,6,3,0,35,44,1,0,0,0,36,37,10,3,0,0,37,38,
        5,6,0,0,38,43,3,6,3,0,39,40,10,2,0,0,40,41,5,7,0,0,41,43,3,6,3,0,
        42,36,1,0,0,0,42,39,1,0,0,0,43,46,1,0,0,0,44,42,1,0,0,0,44,45,1,
        0,0,0,45,5,1,0,0,0,46,44,1,0,0,0,47,48,6,3,-1,0,48,49,3,8,4,0,49,
        61,1,0,0,0,50,51,10,4,0,0,51,52,5,8,0,0,52,60,3,8,4,0,53,54,10,3,
        0,0,54,55,5,9,0,0,55,60,3,8,4,0,56,57,10,2,0,0,57,58,5,10,0,0,58,
        60,3,8,4,0,59,50,1,0,0,0,59,53,1,0,0,0,59,56,1,0,0,0,60,63,1,0,0,
        0,61,59,1,0,0,0,61,62,1,0,0,0,62,7,1,0,0,0,63,61,1,0,0,0,64,73,5,
        12,0,0,65,73,5,13,0,0,66,73,5,14,0,0,67,73,5,15,0,0,68,69,5,2,0,
        0,69,70,3,4,2,0,70,71,5,3,0,0,71,73,1,0,0,0,72,64,1,0,0,0,72,65,
        1,0,0,0,72,66,1,0,0,0,72,67,1,0,0,0,72,68,1,0,0,0,73,9,1,0,0,0,74,
        79,3,4,2,0,75,76,5,11,0,0,76,78,3,4,2,0,77,75,1,0,0,0,78,81,1,0,
        0,0,79,77,1,0,0,0,79,80,1,0,0,0,80,11,1,0,0,0,81,79,1,0,0,0,8,15,
        31,42,44,59,61,72,79
    ]

class MyLanguageParser ( Parser ):

    grammarFileName = "MyLanguage.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'ctrl_v'", "'('", "')'", "'='", "'ctrl_c'", 
                     "'+'", "'-'", "'*'", "'/'", "':'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "INT", "FLOAT", "STRING", "VARIABLE", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_expr = 2
    RULE_term = 3
    RULE_factor = 4
    RULE_exprList = 5

    ruleNames =  [ "program", "statement", "expr", "term", "factor", "exprList" ]

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
    INT=12
    FLOAT=13
    STRING=14
    VARIABLE=15
    WS=16

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
            self.state = 13 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 12
                self.statement()
                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 61446) != 0)):
                    break

            self.state = 17
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
            self.state = 31
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = MyLanguageParser.PrintStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self.match(MyLanguageParser.T__0)
                self.state = 20
                self.match(MyLanguageParser.T__1)
                self.state = 21
                self.exprList()
                self.state = 22
                self.match(MyLanguageParser.T__2)
                pass

            elif la_ == 2:
                localctx = MyLanguageParser.InputStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.match(MyLanguageParser.VARIABLE)
                self.state = 25
                self.match(MyLanguageParser.T__3)
                self.state = 26
                self.match(MyLanguageParser.T__4)
                pass

            elif la_ == 3:
                localctx = MyLanguageParser.AssignVariableStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 27
                self.match(MyLanguageParser.VARIABLE)
                self.state = 28
                self.match(MyLanguageParser.T__3)
                self.state = 29
                self.expr(0)
                pass

            elif la_ == 4:
                localctx = MyLanguageParser.ExprStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 30
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

            self.state = 34
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 44
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 42
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = MyLanguageParser.AddContext(self, MyLanguageParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 36
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 37
                        self.match(MyLanguageParser.T__5)
                        self.state = 38
                        self.term(0)
                        pass

                    elif la_ == 2:
                        localctx = MyLanguageParser.SubtractContext(self, MyLanguageParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 39
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 40
                        self.match(MyLanguageParser.T__6)
                        self.state = 41
                        self.term(0)
                        pass

             
                self.state = 46
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

            self.state = 48
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 61
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 59
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = MyLanguageParser.MultiplyContext(self, MyLanguageParser.TermContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 50
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 51
                        self.match(MyLanguageParser.T__7)
                        self.state = 52
                        self.factor()
                        pass

                    elif la_ == 2:
                        localctx = MyLanguageParser.DivideContext(self, MyLanguageParser.TermContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 53
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 54
                        self.match(MyLanguageParser.T__8)
                        self.state = 55
                        self.factor()
                        pass

                    elif la_ == 3:
                        localctx = MyLanguageParser.DivideContext(self, MyLanguageParser.TermContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 56
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 57
                        self.match(MyLanguageParser.T__9)
                        self.state = 58
                        self.factor()
                        pass

             
                self.state = 63
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
            self.state = 72
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                localctx = MyLanguageParser.IntNumberContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.match(MyLanguageParser.INT)
                pass
            elif token in [13]:
                localctx = MyLanguageParser.FloatNumberContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.match(MyLanguageParser.FLOAT)
                pass
            elif token in [14]:
                localctx = MyLanguageParser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 66
                self.match(MyLanguageParser.STRING)
                pass
            elif token in [15]:
                localctx = MyLanguageParser.VariableContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 67
                self.match(MyLanguageParser.VARIABLE)
                pass
            elif token in [2]:
                localctx = MyLanguageParser.BracketContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 68
                self.match(MyLanguageParser.T__1)
                self.state = 69
                self.expr(0)
                self.state = 70
                self.match(MyLanguageParser.T__2)
                pass
            else:
                raise NoViableAltException(self)

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
        self.enterRule(localctx, 10, self.RULE_exprList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.expr(0)
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 75
                self.match(MyLanguageParser.T__10)
                self.state = 76
                self.expr(0)
                self.state = 81
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
         




