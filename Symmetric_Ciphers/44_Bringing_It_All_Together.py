# Challenge 44: Bringing It All Together
# Full AES Decryption Cycle

def decrypt(ciphertext, round_keys):
    # 1. Initial AddRoundKey
    # 2. 9 Rounds of: InvShiftRows -> InvSubBytes -> AddRoundKey -> InvMixColumns
    # 3. Final Round: InvShiftRows -> InvSubBytes -> AddRoundKey
    pass

print("Implement the inverse functions and loop through round_keys.")