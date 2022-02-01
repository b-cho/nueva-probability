import random

# Counters for the times A is guilty, B is guilty,
# B's blood type matching that of the crime scene, and
# B's blood type not matching, respectively.
A_guilty = 0
B_guilty = 0
B_matches = 0
B_misses = 0
for _ in range(1000000): # Attempt to find valid scenarios 1 million times
    # For each trial...
    guilty = random.randint(1,2) # Randomly decide the guilty suspect with 50/50 probability
    guilty_type = 1 # We know the guilty person has blood type "1"
    A_type = 1 # We also know that A has blood type "1"
    B_type = random.randint(1,10) # B's blood type is "1" with 10% probability (and not "1" with 90% probability)
    if(A_type == guilty_type and guilty == 1): # If A is guilty (and A's blood type matches that of the crime scene)
        A_guilty += 1 # Mark A as guilty for this trial
        if(B_type == guilty_type): # If B's blood type matches that of the crime scene (in this case, A, or type "1")...
            B_matches += 1 # Mark B as matching the crime scene
        else: # Else...
            B_misses += 1 # Mark B as having a different blood type than the crime scene
    elif(A_type == guilty_type and B_type == guilty_type and guilty == 2): # If B is guilty, then B's blood type matches that of the crime scene (and of A's)...
        B_guilty += 1 # So we increment our counters respectively.
        B_matches += 1

print(A_guilty/(A_guilty+B_guilty)) # The answer to (3a)
print(B_matches/(B_matches+B_misses)) # The answer to (3b)