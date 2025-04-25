from MyLanguageParser import MyLanguageParser
from MyLanguageVisitor import MyLanguageVisitor


class ASTVisitor(MyLanguageVisitor):

#assign variable and store them
    def __init__(self):
        self.symbols = {}
    
    def visitAssignVariableStmt(self, ctx):
        var_name = ctx.VARIABLE().getText()
        value = self.visit(ctx.expr())
        self.symbols[var_name] = value
        return value

#print function
    def visitPrintStmt(self, ctx):
        expressions = ctx.exprList().expr()
        for expr in expressions:
            value = self.visit(expr)
            print(value, end=' ')
        print()
        return None

#input
    def visitInputStmt(self, ctx):
        var_name = ctx.VARIABLE().getText()
        value = input()  # Odczytanie wartości z wejścia
        if value.isdigit():
            value = int(value)
        else:
            try:
                value = float(value)
            except ValueError:
                pass
        self.symbols[var_name] = value
        return value 

#fundamental operations 
    def visitAdd(self, ctx):
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        return left + right  

    def visitSubtract(self, ctx):
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        return left - right  
    
    def visitMultiply(self, ctx):
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        return left * right
    
    def visitDivide(self, ctx):
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        if right == 0 :
            raise ValueError('Division by zero, not good...')
        return left / right

    def visitTermExpr(self, ctx):
        return self.visit(ctx.getChild(0))  

# array
    def visitAssignArrayStmt(self, ctx):
        array_name = ctx.VARIABLE().getText()
        elements = [self.visit(expr) for expr in ctx.arrayExpr().exprList().expr()]
        self.symbols[array_name] = elements
        return elements

    def visitArrayAccess(self, ctx):
        array_name = ctx.VARIABLE().getText()
        index = self.visit(ctx.expr())
        if array_name in self.symbols:
            array = self.symbols[array_name]
            if index < len(array):
                return array[index]
            else:
                raise IndexError(f"Index {index} out of bounds for array : {array_name} O_O")
        else:
            raise ValueError(f"Undefined array: {array_name} O_O")
    
    def visitReassignArrayStmt(self, ctx):
        array_name = ctx.VARIABLE().getText()
        index = self.visit(ctx.expr(0))
        value = self.visit(ctx.expr(1))
        if array_name in self.symbols:
            array = self.symbols[array_name]
            if index < len(array):
                array[index] = value
            else:
                raise IndexError(f"Index {index} out of bounds for array : {array_name} O_O")
        else:
            raise ValueError(f"Undefined array: {array_name} O_O")
        return value

# units
    def visitIntNumber(self, ctx):
        return int(ctx.getChild(0).getText())  

    def visitFloatNumber(self, ctx):
        return float(ctx.getChild(0).getText()) 

    def visitBracket(self, ctx):
        bracket = self.visit(ctx.expr())
        return bracket

    def visitString(self, ctx):
        raw = ctx.getText()
        return bytes(raw[1:-1], "utf-8").decode("unicode_escape")
    
    def visitVariable(self, ctx):
        var_name = ctx.getText()
        if var_name not in self.symbols:
            raise ValueError(f"Undefined variable: {var_name} O_O") 
        return self.symbols[var_name]