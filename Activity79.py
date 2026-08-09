def match_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len (word) > 1 and word [0] == word[-1]:
            ctr += 1 
            lst.append(word)
    print("list of words with the first and last charecter same/n",lst)
    return ctr
count = match_words(["abc","cfc","xyz","aba","1221"])
print("the number of words having the first and last charecter the same:",count)
