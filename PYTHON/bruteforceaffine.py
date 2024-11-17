i = 0
j = 0
p = "ab"
c = "gl"
print(p)
print(c)

found = False
t = ""
for i in range(0,26):
		
	
	for j in range(0,26):
		t = ""
		x =(((ord(p[0]) - ord('a'))* i) + j) %26  + ord('a')
		y =(((ord(p[1]) - ord('a'))* i) + j) %26  + ord('a')
		t += chr(x)
		t += chr(y)
		
		print(t)
		if t == "gl":
			found = True
			break
	if found:
		break
print(i,j)		
	
	


n = 1
shifta = i
while (shifta * n) % 26 != 1:
	n += 1
shiftb = j

print(n)

cipher = "XPALASXYFGFUKPXUSOGEUTKCDGEXANMGNVS".lower()
result = ""
for i in cipher:
	x =(((ord(i) -ord('a')) - shiftb) *n) %26  + ord('a')
	print(chr(x))
	result += chr(x)
	
print(result.upper())
