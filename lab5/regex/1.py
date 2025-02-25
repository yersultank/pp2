import re
#1 task
# word=input()
# a=r'ab*'
# if re.findall(a,word):
#     print(f"{word} matches the pattern")
# else:
#     print(f"{word} does not match the pattern")

#2 task  
# word=input()
# a=r'abb{2,3}'
# if re.fullmatch(a,word):
#     print(f"{word} matches the pattern")
# else:
#     print(f"{word} does not match the pattern")

#3 task
# word=input()
# a=r'[a-z]_+[a-z]+'
# match=re.findall(a,word)
# print(match)

#4 task
# word=input()
# a=r'[A-Z]{1}+[a-z]+'
# match=re.findall(a,word)
# print(match)

#5 task
# word=input()
# a=r'a+.b'
# match=re.findall(a,word)
# if re.findall(a,word):
#     print(f"{word} matches the pattern")
# else:
#     print(f"{word} does not match the pattern")

#6 task
# word=input()
# new_word=re.sub(r'[,. ]', '|', word)
# print(new_word)

#7 task
# snake_word=input()
# camel_word=re.sub(r'_',"",snake_word)
# print(camel_word)

#8 task
# word=input()
# new_word=re.split(r'(?=[A-Z])',word)
# print(new_word)
# print(type(new_word))
# for i in new_word:
#     if i=="":
#         new_word.remove(i)
# print(new_word)

#9 task
# word=input()
# new_word=re.sub(r'(?=[A-Z])', " ", word)
# print(new_word)

#10 task
# camel_word=input()
# snake_word=re.findall(r'[A-Z][^A-Z]*', camel_word)
# snake_word='_'.join(snake_word)
# print(snake_word)