
alpha = ['a','b','c','d','e','f','g','h','i','k','l','m','n','o','p','q','r','s','t','v','w','x','y','z']
def convert(plaintext):#to add plain text to the 2d matrix that has the key already in it
    plaintext = plaintext.lower()
    plaintext = plaintext.replace('j','i')
    result = []
    i = 0
    plaintext = plaintext.replace(" ","")
    print(plaintext)
    while i < len(plaintext) :
        if i == len(plaintext) - 1:
            result.append(plaintext[i]+'x')
            break
        if plaintext[i] == plaintext[i+1]:
            result.append(plaintext[i]+'x')
            i +=1
        else :
            result.append(plaintext[i]+plaintext[i+1])
            i += 2
    print(result)
    return result
def shift(posc0,posr0,posc1,posr1):#gives you shift values for different cases for encryption
    
    if posc0 == posc1:
        posr0 = (posr0+1)%5
        posr1 = (posr1+1)%5
        return (posc0,posc1,posr0,posr1)
    if posr0 == posr1:
        posc0 = (posc0+1)%5
        posc1 = (posc1+1)%5
        return (posc0,posc1,posr0,posr1)
    if posc0 != posc1 and posr0 != posr1:
       
     
        return (posc1,posc0,posr0,posr1)
def revshift(posc0,posr0,posc1,posr1):#gives you shift values for different cases for decryption
    
    if posc0 == posc1:
        posr0 = (posr0-1)%5
        posr1 = (posr1-1)%5
        return (posc0,posc1,posr0,posr1)
    if posr0 == posr1:
        posc0 = (posc0-1)%5
        posc1 = (posc1-1)%5
        return (posc0,posc1,posr0,posr1)
    if posc0 != posc1 and posr0 != posr1:
       
     
        return (posc1,posc0,posr0,posr1)  
#TO get a list all characters not in guidance
   
   
beta = []
key = "guidance"
for i in alpha:
    flag = True
    for j in key:
        if i == j:
            flag =False
    if flag:
        beta.append(i)

print(beta)
mat = [["" for _ in range(5)] for _ in range(5)]
cols = 0
rows = 0
for i in key:
    mat[rows][cols] = i 
    cols += 1
    if cols >= 5:
        cols = 0
        rows += 1
        if rows >= 5:
            break
for i in beta:

    mat[rows][cols] = i 
    cols += 1
    if cols >= 5:
        cols = 0
        rows += 1
        if rows >= 5:
            break
print(mat)
plaintext = "The key is hidden under the door pad"#input("Enter plaintext")
result =convert(plaintext)
print(result)
posr0 = 0 
posr1 = 0
posc0 = 0
posc1 = 0
cipher = ""
for i in result:
   
    for j in range(len(mat)):
        for k in range(len(mat[0])):
            if mat[j][k] == i[0]:
                posr0 = j
                posc0 = k
            
            if mat[j][k] == i[1]:
                posr1 = j
                posc1 = k
   
    posc0,posc1,posr0,posr1= shift(posc0,posr0,posc1,posr1)
    cipher += mat[posr0][posc0]
    cipher += mat[posr1][posc1]
  
print(cipher.upper())
   
print("Encrypted cipher : ",cipher.upper())
final = ""
fr = convert(cipher)
print(fr)
for i in fr:
   
    for j in range(len(mat)):
        for k in range(len(mat[0])):
            if mat[j][k] == i[0]:
                posr0 = j
                posc0 = k
            
            if mat[j][k] == i[1]:
                posr1 = j
                posc1 = k
   
    posc0,posc1,posr0,posr1= revshift(posc0,posr0,posc1,posr1)
    final += mat[posr0][posc0]
    final += mat[posr1][posc1]
  
    print(final)
print(final.upper().replace("X",""))
def test():
    print("Hi")

