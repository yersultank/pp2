def is_palindrome(word):
    new_word=word[::-1]
    if word==new_word:
        return True
    else:
        return False
    
a=input("word: ")
print(is_palindrome(a))