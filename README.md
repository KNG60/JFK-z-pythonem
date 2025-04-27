## Quick demo 
Run in bash <code>./compiler.exe input.txt </code>

## How to edit and run project JFK
1.  run ANTLR to generate python & java files:<br>
    in bash <br>
    <code>antlr4 Dlanguage=Python3 MyLanguage.g4 -visitor</code>
    <br>or
    in cmd<br>
    <code>java -jar %ANTLR_JAR% MyLanguage.g4 -Dlanguage=Python3 -visitor</code> 
    
    

2. edit <code>ASTVisitor.py</code> & <code>MyLanguage.g4</code> to add new functionalities
3. Re-run **step 1** to update Gamma rules
4. create example code <code>input.txt</code>

5. run <code>py compiler.py input.txt</code> to check if compiler work properly 
6. Ready compiler convert to .exe file with<code>pyinstaller --onefile compiler.py</code>. Created compiler wil be in new folder <code>dist</code>. Move <code>compiler.exe</code> to the same folder where <code>input.txt</code> is and run <code>./compiler.exe input.txt</code>. All files created with <code>pyinstaller</code> can be deleted and are not needed for <code>compiler.exe</code> to work properly
## Checkout AST tree
<code>antlr4-parse MyLanguage.g4 program input.txt -gui</code>

## Overview compiler structure
To add functionalities, add new statement or something add it to<code>MyLanguage.g4</code> and name it. Then create **def** with the same name in <code>ASTVisitor.py</code> and develop its properties. <br>Checkout other functions and definitions to learn the pattern. Project automatically mach name in .g4 with role in ASTVisitor by function name. To develop compiler only use <code>ASTVisitor.py</code> and <code>MyLanguage.g4</code> 

## Current compiler cover
- functions:<br>
print() : ctrl_v()<br>
input() : x=ctrl_c<br>
basic arithmetic operations<br>

- variables
variable<br>
int<br>
float<br>
string<br>
array<br>


