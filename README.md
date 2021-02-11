# Program-to-find-whether-simple-brackets-in-a-string-are-matched-evenly
Bracket matching program from a string
Algo: find whether the brackets in a string are matching evenly( hackerRank challenge )

Solution:The idea is to pile up "(" and ")" into two separate lists and then compare the length of the lists. I also had another version where I had appended the lists ope and clo with the relevant I which held either ( or ) respectively.


In the second solution, I used a way of keeping track of the current depth of nesting  by pushing opening parentheses onto a stack and popping them from the stack when we encounter a closing parenthesis.
