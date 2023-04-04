input = 'aa      bb, ccc dddd, eee, f ff ff, jjj hh'
tokens = input.split(",")

#print([f"{token.split()[1]} {token.split()[0]}" for token in tokens if len(token.split()) == 2])
print([f"{' '.join(reversed(token.split()))}" for token in tokens if len(token.split()) == 2])
