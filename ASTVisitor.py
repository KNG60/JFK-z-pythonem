from MyLanguageParser import MyLanguageParser
from MyLanguageVisitor import MyLanguageVisitor


class ASTVisitor(MyLanguageVisitor):
    def visitPrintStmt(self, ctx):
        value = self.visit(ctx.expr())  # Evaluate the expression inside print()
        print(value)  # Print to console
        return value  

    def visitAdd(self, ctx):
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        return left + right  

    def visitSubtract(self, ctx):
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        return left - right  

    def visitTermExpr(self, ctx):
        return self.visit(ctx.getChild(0))  

    def visitNumber(self, ctx):
        return int(ctx.getChild(0).getText())  
