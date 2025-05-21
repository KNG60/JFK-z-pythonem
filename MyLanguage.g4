grammar MyLanguage;

program : statement+ EOF ;

statement 
    : ifstatment              # ifElseStmt
    | forstatment            # forStmt
    | functionDecl          # functionDeclStmt
    | structureDecl         # structureDeclStmt
    |'ctrl_v' '('exprList')'  # printStmt
    | VARIABLE '=' 'ctrl_c'    # inputStmt
    | VARIABLE '=' expr     #assignVariableStmt
    | VARIABLE '=' arrayExpr # assignArrayStmt
    | VARIABLE '['expr']' '=' expr # reassignArrayStmt
    | VARIABLE '=' 'new' VARIABLE # structInstantiation
    | VARIABLE '.' VARIABLE '=' expr # structFieldAssign
    | 'return' expr         # returnStmt
    | expr                  # exprStmt
    ;

ifstatment
         : 'if' '(' expr ')' '{' statement* '}' ('else' '{' statement* '}')?
    ;

forstatment
         : 'for' '(' VARIABLE '=' expr 'to' expr ')' '{' statement* '}'
    ;

functionDecl
         : 'function' VARIABLE '(' paramList? ')' '{' statement* '}'
    ;

structureDecl
         : 'struct' VARIABLE '{' structField* '}'
    ;

structField
         : VARIABLE ':' type
    ;

type
         : 'int'
         | 'float'
         | 'string'
         | 'array'
         | VARIABLE
    ;

paramList
         : VARIABLE (',' VARIABLE)*
    ;

expr : expr '+' term        # add
     | expr '-' term        # subtract
     | expr '>' term        # greaterThan
     | expr '<' term        # lessThan
     | expr '>=' term       # greaterEqual
     | expr '<=' term       # lessEqual
     | expr '==' term       # equal
     | expr '!=' term       # notEqual
     | term                 # termExpr
     ;

term : term '*' factor      # multiply
     | term '/' factor      # divide
     | term ':' factor      # divide
     | factor               # factorExpr
     ;

factor : INT                # intNumber
       | FLOAT              # floatNumber
       | STRING             # string
       | VARIABLE           # variable
       | VARIABLE '[' expr ']' # arrayAccess
       | VARIABLE '(' exprList? ')' # functionCall
       | VARIABLE '.' VARIABLE # structAccess
       | arrayExpr          # arrayLiteral
       | '(' expr ')'       # bracket
       ;

arrayExpr : '[' (expr (',' expr)*)? ']';

exprList : expr (',' expr)*;
INT : '-'?[0-9]+ ;
FLOAT : [0-9]+ '.' [0-9]+;
STRING : '"' ~["]* '"' ;
VARIABLE : [a-zA-Z_][a-zA-Z_0-9]*;
WS : [ \t\r\n]+ -> skip ;
