from MyLanguageParser import MyLanguageParser
from MyLanguageVisitor import MyLanguageVisitor


class ASTVisitor(MyLanguageVisitor):
    def visitAdd(self, ctx):
        left = self.visit(ctx.getChild(0))  # Get left operand
        right = self.visit(ctx.getChild(2)) # Get right operand
        return left + right  

    def visitSubtract(self, ctx):
        left = self.visit(ctx.getChild(0))  # Get left operand
        right = self.visit(ctx.getChild(2)) # Get right operand
        return left - right  

    def visitTermExpr(self, ctx):
        return self.visit(ctx.getChild(0))  # Forward to term

    def visitNumber(self, ctx):
        return int(ctx.getChild(0).getText())  # Convert token to integer
