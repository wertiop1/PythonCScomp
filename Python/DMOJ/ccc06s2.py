plaintext1 = input()
ciphertext1 = input()
ciphertext2 = input()
cipherToPlain = {}
for i in range(len(plaintext1)):
    cipherToPlain[ciphertext1[i]] = plaintext1[i]
plaintext2 = ''
for char in ciphertext2:
    if char in cipherToPlain:
        plaintext2 = plaintext2 + cipherToPlain[char]
    else:
        plaintext2 = plaintext2 + '.'
print(plaintext2)