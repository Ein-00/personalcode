known_cipher = "CIW"
known_cipher =known_cipher.lower()
known_plaintext = "YES"
known_plaintext = known_plaintext.lower()
shift = ( ord(known_cipher[0]) - ord(known_plaintext[0])) %26
print(shift)
cipher = "XVIEWYWI".lower()
print(cipher)
result = ""
for i in cipher:
    x = ((ord(i) - ord('a')) - shift) % 26 + ord('a')
    print(chr(x))
    result += chr(x)

print(result.upper())

#Output is TREASUSE