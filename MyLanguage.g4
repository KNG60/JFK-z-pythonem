// MyLanguage.g4
grammar MyLanguage;

program : statement+ ;

statement : expr EOF ;

expr : expr '+' term   # add
     | expr '-' term   # subtract
     | term            # termExpr
     ;

term : INT             # number
     ;

INT : [0-9]+ ;
WS : [ \t\r\n]+ -> skip ;
