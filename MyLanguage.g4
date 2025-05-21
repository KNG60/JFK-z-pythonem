grammar MyLanguage;

program : statement+ EOF ;

statement 
    : ifstatment              # ifElseStmt
    | forstatment            # forStmt
    | functionDecl          # functionDeclStmt
    | structureDecl         # structureDeclStmt
    | classDecl            # classDeclStmt
    |'ctrl_v' '('exprList')'  # printStmt
    | VARIABLE '=' 'ctrl_c'    # inputStmt
    | VARIABLE '=' expr     #assignVariableStmt
    | VARIABLE '=' arrayExpr # assignArrayStmt
    | VARIABLE '['expr']' '=' expr # reassignArrayStmt
    | VARIABLE '=' 'new' VARIABLE # structInstantiation
    | VARIABLE '.' VARIABLE '=' expr # structFieldAssign
    | 'oddaj' expr         # returnStmt
    | expr                  # exprStmt
    ;

ifstatment
         : 'naprawde' '(' expr ')' '{' statement* '}' ('zartowalem' '{' statement* '}')?
    ;

forstatment
         : 'cyklon' '(' VARIABLE '=' expr 'oko' expr ')' '{' statement* '}'
    ;

functionDecl
         : 'rozkaz_arr' VARIABLE '(' paramList? ')' '{' statement* '}'
    ;

structureDecl
         : 'lawica' VARIABLE '{' structField* '}'
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
       | VARIABLE '.' VARIABLE '(' exprList? ')' # methodCall
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

classDecl
    : 'klan' VARIABLE '{' classMember* '}'
    ;

classMember
    : VARIABLE ':' type    # classField
    | functionDecl         # classMethod
    ;
