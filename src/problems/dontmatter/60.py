def decode(word):
    output = ''
    i = 0
    while i < len(word):
        if i+1 < len(word) and word[i] == 'p' and word[i+1] != 'p':
            output += word[i+1]
        elif i+2 < len(word) and word[i] == 'p' and word[i+1] in 'pP':
            output += 'p'
            i += 1
        i += 1
    return output

s = input().split(" ")
decoded_s = [decode(word) for word in s]
print(' '.join([w for w in decoded_s]))