"""display the string "Hello" using while loop and skip the iteration for the letters e and o"""
i = 0
s="Hello"
while (i < len(s)):
    if (s[i] == 'e' or s[i]=='o'):
        i = i + 1
        continue
    print(s[i],end="")
    i = i + 1