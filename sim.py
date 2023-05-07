""" Pvalue = 199
Gvalue = 127
Bob_pbKey = 0
Alice_pbKey = 0
Alice_prkey = int(input('add Alice\'s private key: '))
Bob_prkey = int(input('add Bob\'s private key: ')) """


def publicValue(G, P, prKey):
    key = (G**prKey) % P
    return key

def symmetricKeys(p_value, prKey ,P):
    x = (p_value**prKey) % P
    return x

def Diffie_Hellman(G,P,A_key,B_key):
    #B = bobs A = alice
	p_key = 0
	x = publicValue(G,P,A_key)
	y = publicValue(G,P,B_key) 
	ka = symmetricKeys(x, B_key, P)
	kb = symmetricKeys(y, A_key, P) 
	if(ka == kb):
		p_key = kb
	return p_key
    


def toHex(a):
    l, m = [], []
    for i in a:
        l.append(ord(i))
    for i in l:
        m.append(hex(i)[2:])
    return m

def transform(x):
	x_value = str(x) 
	check = ''
	if(len(x_value) == 1):
		x_value = x_value+'C'
		for i in range(8):
			check+=x_value
	elif(len(x_value) == 2):
		x_value = x_value+'DD'
		for i in range(4):
			check+=x_value
	elif(len(x_value) == 3):
		x_value = x_value+'F'
		for i in range(5):
			check+=x_value
	else:
		check = '0'
	return check

def OGform(x):
	x_value = str(x)
	check = []
	chunks = [x_value[i:i+16] for i in range(0, len(x_value), 16)]
	for  a, i in enumerate(chunks):
		if(len(i)<16):
			lack = 16 - len(i)
			for x in range(lack):
				i +='@'
			chunks[a] = i
			break
			
			
	return chunks

		

dh =   Diffie_Hellman(127, 199, 57, 167)
print(dh)
value = transform(dh)
print(value)
print(toHex(str(value)))
#The Mandalorian
#print(toHex('The Mandalorian'))
print(OGform('The Mandalorian Must Always Recite, This is The Way!     '))

 

    


