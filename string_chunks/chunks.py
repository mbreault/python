## process a string in chunks of length N

long_str = "The quick brown fox jumped over the lazy dog"

for i in range(0, len(long_str) - 1, 4900):
    print(long_str[i:i+4900])
