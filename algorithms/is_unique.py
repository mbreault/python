## Determine if a string has all unique characters without using additional data structures

def is_unique(s):
    return_value = True

    l = len(s)

    for i in range(l):
        for j in range(l):
            if i != j and s[i] == s[j]:
               return False

    return True

print(is_unique("xyzx"))