# Diffi-Hellman

import random

# g & p are public
g = random.randrange(3, 1000)
p = random.randrange(3, 1000)
print("g: ",g)
print("p: ",p)

############### USER A ###############
# Private random number X_A 
X_A = random.randrange(3, 1000)
print("X: ",X_A)

# Calculate his public key R_A
R_A = (g ** X_A) % p
print("R_A: ",R_A)

############### USER B ###############
# Private random number Y_B 
Y_B = random.randrange(3, 1000)
print("Y: ",Y_B)

# Calculate his public key R_A
R_B = (g ** Y_B) % p
print("R_B: ",R_B)

# USER_A has R_B & USER_B has R_A --> Use them to generate the same key
############### KEY: USER A ###############
K_A = (R_B ** X_A) % p
print("\nKey Generated by User A is: ",K_A)

############### KEY: USER B ###############
K_B = (R_A ** Y_B) % p
print("Key Generated by User B is: ",K_B)

############### TEST ###############
if K_A == K_B:
    print("\nGOOD NEWS!!!!!!! \nTHE 2 USERS SHARED THE SECRET KEY SUCCESSFULLY :) \n")
else:
    print("UNFORTUNATELY :( \nTHE 2 KEYS ARE NOT MATCHED!!!\n")

############### KEY ###############
K = (g ** (X_A * Y_B)) % p
print("The private shared key is: ",K)