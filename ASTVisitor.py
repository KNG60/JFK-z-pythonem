from MyLanguageParser import MyLanguageParser
from MyLanguageVisitor import MyLanguageVisitor


class ASTVisitor(MyLanguageVisitor):

    # assign variable and store them
    def __init__(self):
        self.symbols = {}  # Global variables
        self.functions = {}  # Function definitions
        self.structures = {}  # Structure definitions
        self.current_scope = None  # Current function scope

    def create_scope(self):
        return {'parent': self.current_scope, 'symbols': {}}

    def get_variable(self, name):
        # First check in current scope
        if self.current_scope and name in self.current_scope['symbols']:
            return self.current_scope['symbols'][name]
        # Then check in global scope
        return self.symbols.get(name)

    def set_variable(self, name, value):
        if self.current_scope:
            self.current_scope['symbols'][name] = value
        else:
            self.symbols[name] = value

    def visitFunctionDeclStmt(self, ctx):
        func_name = ctx.functionDecl().VARIABLE().getText()
        # Store function definition
        self.functions[func_name] = {
            'params': [param.getText() for param in ctx.functionDecl().paramList().VARIABLE()] if ctx.functionDecl().paramList() else [],
            'body': ctx.functionDecl().statement()
        }
        return None

    def visitFunctionCall(self, ctx):
        func_name = ctx.VARIABLE().getText()
        if func_name not in self.functions:
            raise ValueError(f"Undefined function: {func_name}")

        # Get function definition
        func_def = self.functions[func_name]

        # Get arguments
        args = []
        if ctx.exprList():
            args = [self.visit(arg) for arg in ctx.exprList().expr()]

        # Check argument count
        if len(args) != len(func_def['params']):
            raise ValueError(
                f"Function {func_name} expects {len(func_def['params'])} arguments, got {len(args)}")

        # Create new scope for function
        old_scope = self.current_scope
        self.current_scope = self.create_scope()

        # Set parameters in new scope
        for param_name, arg_value in zip(func_def['params'], args):
            self.current_scope['symbols'][param_name] = arg_value

        # Execute function body
        result = None
        try:
            for stmt in func_def['body']:
                result = self.visit(stmt)
        except ReturnValue as ret:
            result = ret.value

        # Restore old scope
        self.current_scope = old_scope
        return result

    def visitVariable(self, ctx):
        var_name = ctx.getText()
        value = self.get_variable(var_name)
        if value is None:
            raise ValueError(f"Undefined variable: {var_name}")
        return value

    def visitAssignVariableStmt(self, ctx):
        var_name = ctx.VARIABLE().getText()
        value = self.visit(ctx.expr())
        self.set_variable(var_name, value)
        return value

# ifElseStmt

    def visitIfElseStmt(self, ctx):
        # Get the condition expression from the if statement
        condition = self.visit(ctx.ifstatment().expr())

        # Get all statements in the if block
        if_statements = ctx.ifstatment().statement()
        num_statements = len(if_statements)

        # If condition is true, execute if block
        if condition:
            # Visit statements in the if block (first half of statements)
            for stmt in if_statements[:num_statements//2]:
                self.visit(stmt)
        # If there's an else block and condition is false
        elif ctx.ifstatment().getChildCount() > 5:  # Check if else block exists
            # Visit statements in the else block (second half of statements)
            for stmt in if_statements[num_statements//2:]:
                self.visit(stmt)

        return None

# print function
    def visitPrintStmt(self, ctx):
        expressions = ctx.exprList().expr()
        for expr in expressions:
            value = self.visit(expr)
            print(value, end=' ')
        print()
        return None

# input
    def visitInputStmt(self, ctx):
        var_name = ctx.VARIABLE().getText()
        value = input()  # Odczytanie wartości z wejścia
        if value.isdigit():
            value = int(value)
        else:
            try:
                value = float(value)
            except ValueError:
                str(value)
        self.symbols[var_name] = value
        return value

# fundamental operations
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
        if right == 0:
            raise ValueError('Division by zero, not good...')
        return left / right

    def visitTermExpr(self, ctx):
        return self.visit(ctx.getChild(0))

# array
    def visitArrayExpr(self, ctx):
        elements = []
        # Get all expressions in the array
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if isinstance(child, MyLanguageParser.ExprContext):
                value = self.visit(child)
                elements.append(value)
        return elements

    def visitAssignArrayStmt(self, ctx):
        var_name = ctx.VARIABLE().getText()
        elements = self.visit(ctx.arrayExpr())
        self.set_variable(var_name, elements)
        return elements

    def visitArrayAccess(self, ctx):
        array_name = ctx.VARIABLE().getText()
        index = self.visit(ctx.expr())
        array = self.get_variable(array_name)
        if array is None:
            raise ValueError(f"Undefined array: {array_name}")
        if not isinstance(array, list):
            raise ValueError(f"Variable {array_name} is not an array")
        if index < 0 or index >= len(array):
            raise ValueError(
                f"Index {index} out of bounds for array {array_name}")
        return array[index]

    def visitReassignArrayStmt(self, ctx):
        array_name = ctx.VARIABLE().getText()
        index = self.visit(ctx.expr(0))
        value = self.visit(ctx.expr(1))
        array = self.get_variable(array_name)
        if array is None:
            raise ValueError(f"Undefined array: {array_name}")
        if not isinstance(array, list):
            raise ValueError(f"Variable {array_name} is not an array")
        if index < 0 or index >= len(array):
            raise ValueError(
                f"Index {index} out of bounds for array {array_name}")
        array[index] = value
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

    def visitGreaterThan(self, ctx):
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        return left > right

    def visitLessThan(self, ctx):
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        return left < right

    def visitGreaterEqual(self, ctx):
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        return left >= right

    def visitLessEqual(self, ctx):
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        return left <= right

    def visitEqual(self, ctx):
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        return left == right

    def visitNotEqual(self, ctx):
        left = self.visit(ctx.getChild(0))
        right = self.visit(ctx.getChild(2))
        return left != right

    def visitForStmt(self, ctx):
        # Get the loop variable name
        var_name = ctx.forstatment().VARIABLE().getText()

        # Get start and end values
        start_value = self.visit(ctx.forstatment().expr(0))
        end_value = self.visit(ctx.forstatment().expr(1))

        # Get the statements to execute in the loop
        statements = ctx.forstatment().statement()

        # Execute the loop
        for i in range(start_value, end_value + 1):
            # Set the loop variable
            self.symbols[var_name] = i

            # Execute the statements in the loop body
            for stmt in statements:
                self.visit(stmt)

        return None

    def visitReturnStmt(self, ctx):
        return self.visit(ctx.expr())

    def visitStructureDeclStmt(self, ctx):
        struct_name = ctx.structureDecl().VARIABLE().getText()
        fields = {}

        # Process each field in the structure
        for field in ctx.structureDecl().structField():
            field_name = field.VARIABLE().getText()
            # Get the type text directly from the type rule
            # Get the type after the ':'
            field_type = field.getChild(2).getText()
            fields[field_name] = field_type

        self.structures[struct_name] = fields
        return None

    def visitStructFieldAssign(self, ctx):
        struct_var = ctx.VARIABLE(0).getText()
        field_name = ctx.VARIABLE(1).getText()
        value = self.visit(ctx.expr())

        # Get the structure instance
        struct_instance = self.get_variable(struct_var)
        if struct_instance is None:
            raise ValueError(f"Undefined structure variable: {struct_var}")

        # Check if the field exists in the structure definition
        struct_type = None
        for name, fields in self.structures.items():
            if struct_instance is self.get_variable(name):
                struct_type = name
                break

        if struct_type and field_name in self.structures[struct_type]:
            field_type = self.structures[struct_type][field_name]
            # Validate type if it's an array
            if field_type == 'array' and not isinstance(value, list):
                raise ValueError(f"Field {field_name} must be an array")

        # Update the field value
        struct_instance[field_name] = value
        return value

    def visitStructAccess(self, ctx):
        struct_var = ctx.VARIABLE(0).getText()
        field_name = ctx.VARIABLE(1).getText()

        # Get the structure instance
        struct_instance = self.get_variable(struct_var)
        if struct_instance is None:
            raise ValueError(f"Undefined structure variable: {struct_var}")

        # Get the field value
        if field_name not in struct_instance:
            raise ValueError(
                f"Field {field_name} not found in structure {struct_var}")

        return struct_instance[field_name]

    def create_struct_instance(self, struct_name):
        if struct_name not in self.structures:
            raise ValueError(f"Undefined structure type: {struct_name}")

        # Create a new instance with default values based on field types
        instance = {}
        for field_name, field_type in self.structures[struct_name].items():
            if field_type == 'int':
                instance[field_name] = 0
            elif field_type == 'float':
                instance[field_name] = 0.0
            elif field_type == 'string':
                instance[field_name] = ""
            elif field_type == 'array':
                instance[field_name] = []
            else:
                # For custom types, create a new instance
                instance[field_name] = self.create_struct_instance(field_type)

        return instance

    def visitStructInstantiation(self, ctx):
        # The variable to store the instance
        var_name = ctx.VARIABLE(0).getText()
        struct_name = ctx.VARIABLE(1).getText()  # The structure type

        # Create a new instance of the structure
        instance = self.create_struct_instance(struct_name)

        # Store the instance in the current scope
        self.set_variable(var_name, instance)
        return instance


class ReturnValue(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__()
