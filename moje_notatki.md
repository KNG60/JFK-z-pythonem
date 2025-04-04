1. Create MyLanguage.g4 with grammar

2. Run ANTLR in cmd in this project folder to generate Java files: 
    <code>java -jar %ANTLR_JAR% MyLanguage.g4 -Dlanguage=Python3 -visitor</code>  

3. Stwórz plik compiler.py oraz ASTVisitor.py
4. stworz input.txt z przykadem
