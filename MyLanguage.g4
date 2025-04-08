grammar MyLanguage;

program : statement+ EOF ;

statement 
    : 'ctrl_v' '('exprList')'  # printStmt
    | VARIABLE '=' 'ctrl_c'    # inputStmt
    | VARIABLE '=' expr     #assignVariableStmt
    | expr                  # exprStmt
    ;

expr : expr '+' term        # add
     | expr '-' term        # subtract
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
       | '(' expr ')'       # bracket
       ;

exprList : expr (',' expr)*;

INT : [0-9]+ ;
FLOAT : [0-9]+ '.' [0-9]+;
STRING : '"' ~["]* '"' ;
VARIABLE : [a-zA-Z_][a-zA-Z_0-9]*;
WS : [ \t\r\n]+ -> skip ;
