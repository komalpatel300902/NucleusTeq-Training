# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
pattern = "\d\s(C|CPP|JAVA|PYTHON|PERL|PHP|RUBY|CSHARP|HASKELL|CLOJURE|BASH|SCALA|ERLANG|CLISP|LUA|BRAINFUCK|JAVASCRIPT|GO|D|OCAML|R|PASCAL|SBCL|DART|GROOVY|OBJECTIVEC)$"
n = int(input(""))
for x in range(n):
    a = input("")
    if re.search(pattern, a):
        print("VALID")
    else:
        print("INVALID")
    