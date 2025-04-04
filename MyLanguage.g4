grammar MyLanguage;

program : statement+ EOF ;

statement 
    : 'print' '(' expr ')'  # printStmt
    | expr                  # exprStmt
    ;

expr : expr '+' term   # add
     | expr '-' term   # subtract
     | term            # termExpr
     ;

term : INT             # number
     ;

INT : [0-9]+ ;
WS : [ \t\r\n]+ -> skip ;
