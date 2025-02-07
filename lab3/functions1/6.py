def reverse_sentence(sentence):
    sentence=list(sentence.split())
    sentence.reverse()
    for i in sentence:
        print(i, end=" ")
a=str(input("type your sentence: "))
reverse_sentence(a)
