import random
lower = random.getrandbits(16)
upper = random.getrandbits(16)

# Prime list creating
prime_list = list()
for num in range (lower,upper+1):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
            prime_list.append(num)

# print(prime_list)
p = random.choice(prime_list)
q = random.choice(prime_list)
print( f''' p is {p}
 q is {q}''')

N = p*q
print( f' N is {N}')

phi_N = (p-1)*(q-1)
print(f" phi_N is {phi_N}")

# lower_cp = 100
# upper_cp= 1000

cp_list = list()
for cp_num in range (lower,upper):
    if cp_num>1:
        for i in range(2,cp_num):
            if (cp_num%i)==0:
                break
        else:
            cp_list.append(cp_num)

def gcd(phi_N, i):
    # Everything divides 0
    if (i == 0):
        return phi_N
    return gcd(i, phi_N % i)


CP = cp_list
for i in CP:
    if (gcd(phi_N, i)):
        print('GCD of', phi_N, 'and', i, 'is', gcd(phi_N, i))
        break

    else:
        print("no e")

e = print(f' e is {i}')




