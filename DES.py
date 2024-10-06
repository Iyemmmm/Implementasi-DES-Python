initial_permutation = [
    58,50,42,34,26,18,10,2,
    60,52,44,36,28,20,12,4,
    62,54,46,38,30,22,14,6,
    64,56,48,40,32,24,16,8,
    57,49,41,33,25,17,9,1,
    59,51,43,35,27,19,11,3,
    61,53,45,37,29,21,13,5,
    63,55,47,39,31,23,15,7
]

PC_1 = [
    57,49,41,33,25,17,9,
    1,58,50,42,34,26,18,
    10,2,59,51,43,35,27,
    19,11,3,60,52,44,36,
    63,55,47,39,31,23,15,
    7,62,54,46,38,30,22,
    14,6,61,53,45,37,29,
    21,13,5,28,20,12,4
]

PC_2 = [
    14, 17, 11, 24, 1, 5,  
    3, 28, 15, 6,  21, 10, 
    23, 19, 12, 4, 26, 8,  
    16, 7,  27, 20, 13, 2,  
    41, 52, 31, 37, 47, 55, 
    30, 40, 51, 45, 33, 48, 
    44, 49, 39, 56, 34, 53, 
    46, 42, 50, 36, 29, 32
]

computer_binary = [
    0, 1, 0, 0, 0, 0, 1, 1, 
    0, 1, 0, 0, 1, 1, 1, 1, 
    0, 1, 0, 0, 1, 1, 0, 1, 
    0, 1, 0, 1, 0, 0, 0, 0, 
    0, 1, 0, 1, 0, 1, 0, 1, 
    0, 1, 0, 1, 0, 1, 0, 0, 
    0, 1, 0, 0, 0, 1, 0, 1, 
    0, 1, 0, 1, 0, 0, 1, 0
]

# ASCII plain text=COMPUTER
key = [
    0, 1, 1, 0, 1, 0, 1, 1,  # 'k'
    0, 1, 1, 0, 1, 1, 1, 1,  # 'o'
    0, 1, 1, 0, 1, 1, 0, 0,  # 'l'
    0, 1, 1, 0, 1, 0, 0, 1,  # 'i'
    0, 1, 1, 1, 0, 0, 1, 1,  # 's'
    0, 1, 1, 0, 0, 0, 0, 1,  # 'a'
    0, 1, 1, 0, 1, 1, 1, 0,  # 'n'
    0, 1, 1, 0, 0, 1, 0, 1   # 'e'
]

matrix_ekspansi = [
    32,1,2,3,4,5,
    4,5,6,7,8,9,
    8,9,10,11,12,13,
    12,13,14,15,16,17,
    16,17,18,19,20,21,
    20,21,22,23,24,25,
    24,25,26,27,28,29,
    28,29,30,31,32,1
]
    # P-Box permutation order
p_order = [
    16, 7, 20, 21, 29, 12, 28, 17,
    1, 15, 23, 26,5, 8, 31, 10,
    2, 8, 24, 14,32, 27, 3, 9,
    19, 13, 30, 6,22, 11, 4, 25
]


invers_permutasi = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

def string_to_binary_array(input_string):
    binary_array = []
    for char in input_string:
        # Mengonversi karakter menjadi nilai ASCII
        ascii_value = ord(char)
        # Mengonversi nilai ASCII menjadi biner 8-bit
        binary_value = format(ascii_value, '08b')
        # Memasukkan setiap bit ke dalam array
        binary_array.extend(int(bit) for bit in binary_value)
    return binary_array

def PC_1_permutation(key_block):
    hasil = [0] * 56    
    for i in range(56):
        hasil[i] = key_block[PC_1[i]-1]
    return hasil

def PC_2_permutation(key_block):
    hasil = [0] * 48    
    for i in range(48):
        hasil[i] = key_block[PC_2[i]-1]
    return hasil

def split_block(key_block):
    half = len(key_block) // 2
    C = key_block[:half]
    D = key_block[half:]
    return C, D

def left_shift(block):
    return block[1:] + [block[0]]

def combine(block1, block2):
    return block1 + block2

def ekspansi(block):
    hasil = [0] * 48    
    for i in range(48):
        hasil[i] = block[matrix_ekspansi[i]-1]
    return hasil

def xor(array1, array2):
    return [b1 ^ b2 for b1, b2 in zip(array1, array2)]

def split_6bit(array):
    return [array[i:i + 6] for i in range(0, len(array), 6)]

def sbox(input_bits, sbox_number):
    row = (input_bits[0] << 1) | input_bits[5]
    col = (input_bits[1] << 3) | (input_bits[2] << 2) | (input_bits[3] << 1) | input_bits[4]

    # Definisi S-boxes
    sboxes = {
        1: [
            [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
            [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
            [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
            [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
        ],
        2: [
            [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
            [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
        ],
        3: [
            [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
            [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
            [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
        ],
        4: [
            [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
            [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
            [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
        ],
        5: [
            [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
            [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
            [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
        ],
        6: [
            [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
            [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
            [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
            [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
        ],
        7: [
            [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
            [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
        ],
        8: [
            [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
            [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
            [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
        ]
    }

    # Ambil nilai dari S-box yang sesuai
    sbox_table = sboxes[sbox_number]
    output_value = sbox_table[row][col]

    # Mengonversi output ke biner (4 bit)
    output_bits = [(output_value >> i) & 1 for i in range(3, -1, -1)]  # Menghasilkan 4 bit

    return output_bits

def pbox(input_bits):

    # Create the output array for the permuted bits
    output_bits = [0] * 32

    # Apply the P-Box permutation
    for i in range(32):
        output_bits[i] = input_bits[p_order[i] - 1]

    return output_bits

def final(block):
    hasil = [0] * 64    
    for i in range(64):
        hasil[i] = block[invers_permutasi[i]-1]
    return hasil



input_key=input("Masukkan nilai key: ")
binary_key=string_to_binary_array(input_key)
print(binary_key)

# Generasi K1
binary_key_final = PC_1_permutation(binary_key)
C0, D0 = split_block(binary_key_final)
C1 = left_shift(C0)
D1 = left_shift(D0)
cr_combine1 = combine(C1, D1)
K1 = PC_2_permutation(cr_combine1)

# Generasi K2
C2 = left_shift(C1)
D2 = left_shift(D1)
cr_combine2 = combine(C2, D2)
K2 = PC_2_permutation(cr_combine2)

# Generasi K3
C3 = left_shift(left_shift(C2))
D3 = left_shift(left_shift(D2))
cr_combine3 = combine(C3, D3)
K3 = PC_2_permutation(cr_combine3)

# Generasi K4
C4 = left_shift(left_shift(C3))
D4 = left_shift(left_shift(D3))
cr_combine4 = combine(C4, D4)
K4 = PC_2_permutation(cr_combine4)

# Generasi K5
C5 = left_shift(left_shift(C4))
D5 = left_shift(left_shift(D4))
cr_combine5 = combine(C5, D5)
K5 = PC_2_permutation(cr_combine5)

# Generasi K6
C6 = left_shift(left_shift(C5))
D6 = left_shift(left_shift(D5))
cr_combine6 = combine(C6, D6)
K6 = PC_2_permutation(cr_combine6)

# Generasi K7
C7 = left_shift(left_shift(C6))
D7 = left_shift(left_shift(D6))
cr_combine7 = combine(C7, D7)
K7 = PC_2_permutation(cr_combine7)

# Generasi K8
C8 = left_shift(left_shift(C7))
D8 = left_shift(left_shift(D7))
cr_combine8 = combine(C8, D8)
K8 = PC_2_permutation(cr_combine8)

# Generasi K9
C9 = left_shift(C8)
D9 = left_shift(D8)
cr_combine9 = combine(C9, D9)
K9 = PC_2_permutation(cr_combine9)

# Generasi K10
C10 = left_shift(left_shift(C9))
D10 = left_shift(left_shift(D9))
cr_combine10 = combine(C10, D10)
K10 = PC_2_permutation(cr_combine10)

# Generasi K11
C11 = left_shift(left_shift(C10))
D11 = left_shift(left_shift(D10))
cr_combine11 = combine(C11, D11)
K11 = PC_2_permutation(cr_combine11)

# Generasi K12
C12 = left_shift(left_shift(C11))
D12 = left_shift(left_shift(D11))
cr_combine12 = combine(C12, D12)
K12 = PC_2_permutation(cr_combine12)

# Generasi K13
C13 = left_shift(left_shift(C12))
D13 = left_shift(left_shift(D12))
cr_combine13 = combine(C13, D13)
K13 = PC_2_permutation(cr_combine13)

# Generasi K14
C14 = left_shift(left_shift(C13))
D14 = left_shift(left_shift(D13))
cr_combine14 = combine(C14, D14)
K14 = PC_2_permutation(cr_combine14)

# Generasi K15
C15 = left_shift(left_shift(C14))
D15 = left_shift(left_shift(D14))
cr_combine15 = combine(C15, D15)
K15 = PC_2_permutation(cr_combine15)

# Generasi K16
C16 = left_shift(C15)
D16 = left_shift(D15)
cr_combine16 = combine(C16, D16)
K16 = PC_2_permutation(cr_combine16)

# Cetak Hasil
print("K1:", K1)
print("K2:", K2)
print("K3:", K3)
print("K4:", K4)
print("K5:", K5)
print("K6:", K6)
print("K7:", K7)
print("K8:", K8)    
print("K9:", K9)
print("K10:", K10)
print("K11:", K11)
print("K12:", K12)
print("K13:", K13)
print("K14:", K14)
print("K15:", K15)
print("K16:", K16)


# Iterasi 1
L0, R0 = split_block(computer_binary)
print("L0 R0: ",L0,R0)
E_R0 = ekspansi(R0)
A1 = xor(E_R0, K1)
result = split_6bit(A1)
B1 = []
for i in range(8):
    output = sbox(result[i], i + 1)
    B1.extend(output)
B1_pbox=pbox(B1)
L1 = R0
R1 = xor(L0, B1_pbox)
print("L1 R1: ",L1,R1)

# Iterasi 2
E_R1 = ekspansi(R1)
A2 = xor(E_R1, K2)
result = split_6bit(A2)
B2 = []
for i in range(8):
    output = sbox(result[i], i + 1)
    B2.extend(output)
B2_pbox=pbox(B2)
L2 = R1
R2 = xor(L1, B2_pbox)

# Iterasi 3
E_R2 = ekspansi(R2)
A3 = xor(E_R2, K3)
result = split_6bit(A3)
B3 = []
for i in range(8):
    output = sbox(result[i], i + 1)
    B3.extend(output)
B3_pbox=pbox(B3)
L3 = R2
R3 = xor(L2, B3_pbox)

# Iterasi 4
E_R3 = ekspansi(R3)
A4 = xor(E_R3, K4)
result = split_6bit(A4)
B4 = []
for i in range(8):
    output = sbox(result[i], i + 1)
    B4.extend(output)
B4_pbox=pbox(B4)
L4 = R3
R4 = xor(L3, B4_pbox)

# Iterasi 5
E_R4 = ekspansi(R4)
A5 = xor(E_R4, K5)
result = split_6bit(A5)
B5 = []
for i in range(8):
    output = sbox(result[i], i + 1)
    B5.extend(output)
B5_pbox=pbox(B5)
L5 = R4
R5 = xor(L4, B5_pbox)

# Iterasi 6
E_R5 = ekspansi(R5)
A6 = xor(E_R5, K6)
result = split_6bit(A6)
B6 = []
for i in range(8):
    output = sbox(result[i], i + 1)
    B6.extend(output)
B6_pbox=pbox(B6)
L6 = R5
R6 = xor(L5, B6_pbox)

# Iterasi 7
E_R6 = ekspansi(R6)
A7 = xor(E_R6, K7)
result = split_6bit(A7)
B7 = []
for i in range(8):
    output = sbox(result[i], i + 1)
    B7.extend(output)
B7_pbox=pbox(B7)
L7 = R6
R7 = xor(L6, B7_pbox)

# Iterasi 8
E_R7 = ekspansi(R7)
A8 = xor(E_R7, K8)
result = split_6bit(A8)
B8 = []
for i in range(8):
    output = sbox(result[i], i + 1)
    B8.extend(output)
B8_pbox=pbox(B8)
L8 = R7
R8 = xor(L7, B8_pbox)

# Iterasi 9
E_R8 = ekspansi(R8)
A9 = xor(E_R8, K9)
result = split_6bit(A9)
B9 = []
for i in range(8):
    output = sbox(result[i], i + 1)
    B9.extend(output)
B9_pbox=pbox(B9)
L9 = R8
R9 = xor(L8, B9_pbox)

# Iterasi 10
E_R9 = ekspansi(R9)
A10 = xor(E_R9, K10)
result = split_6bit(A10)
B10 = []
for i in range(8):
    output = sbox(result[i], i + 1)
    B10.extend(output)
B10_pbox=pbox(B10)
L10 = R9
R10 = xor(L9, B10_pbox)

# Iterasi 11
E_R10 = ekspansi(R10)
A11 = xor(E_R10, K11)
result = split_6bit(A11)
B11 = []
for i in range(8):
    output = sbox(result[i], i + 1)
    B11.extend(output)
B11_pbox=pbox(B11)
L11 = R10
R11 = xor(L10, B11_pbox)

# Iterasi 12
E_R11 = ekspansi(R11)
A12 = xor(E_R11, K12)
result = split_6bit(A12)
B12 = []
for i in range(8):
    output = sbox(result[i], i + 1)
    B12.extend(output)
B12_pbox=pbox(B12)
L12 = R11
R12 = xor(L11, B12_pbox)

# Iterasi 13
E_R12 = ekspansi(R12)
A13 = xor(E_R12, K13)
result = split_6bit(A13)
B13 = []
for i in range(8):
    output = sbox(result[i], i + 1)
    B13.extend(output)
B13_pbox=pbox(B13)
L13 = R12
R13 = xor(L12, B13_pbox)

# Iterasi 14
E_R13 = ekspansi(R13)
A14 = xor(E_R13, K14)
result = split_6bit(A14)
B14 = []
for i in range(8):
    output = sbox(result[i], i + 1)
    B14.extend(output)
B14_pbox=pbox(B14)
L14 = R13
R14 = xor(L13, B14_pbox)

# Iterasi 15
E_R14 = ekspansi(R14)
A15 = xor(E_R14, K15)
result = split_6bit(A15)
B15 = []
for i in range(8):
    output = sbox(result[i], i + 1)
    B15.extend(output)
B15_pbox=pbox(B15)
L15 = R14
R15 = xor(L14, B15_pbox)

# Iterasi 16
E_R15 = ekspansi(R15)
A16 = xor(E_R15, K16)
result = split_6bit(A16)
B16 = []
for i in range(8):
    output = sbox(result[i], i + 1)
    B16.extend(output)
B16_pbox=pbox(B16)
L16 = R15
R16 = xor(L15, B16_pbox)

print("L1:", L1)
print("L2:", L2)
print("L3:", L3)
print("L4:", L4)
print("L5:", L5)
print("L6:", L6)
print("L7:", L7)
print("L8:", L8)    
print("L9:", L9)
print("L10:", L10)
print("L11:", L11)
print("L12:", L12)
print("L13:", L13)
print("L14:", L14)
print("L15:", L15)
print("L16:", L16)

print("R1:", R1)
print("R2:", R2)
print("R3:", R3)
print("R4:", R4)
print("R5:", R5)
print("R6:", R6)
print("R7:", R7)
print("R8:", R8)    
print("R9:", R9)
print("R10:", R10)
print("R11:", R11)
print("R12:", R12)
print("R13:", R13)
print("R14:", R14)
print("R15:", R15)
print("R16:", R16)

final_block = combine(L16, R16)
ciphertext = final(final_block)
print("final_block",final_block)
print("FINAL: ", ciphertext)

# E_R0=[
#     1,0,0,0,0,0,
#     0,0,0,0,0,0,
#     0,0,0,0,0,0,
#     0,0,0,0,0,0,
#     0,0,0,0,0,0,
#     0,0,1,1,0,1,
#     0,1,0,0,0,0,
#     0,0,0,1,1,0
# ]
# K1=[
#     0,0,0,1,1,0,
#     1,1,0,0,0,0,
#     0,0,1,0,1,1,
#     1,0,1,1,1,1,
#     1,1,1,1,1,1,
#     0,0,0,1,1,1,
#     0,0,0,0,0,1,
#     1,1,0,0,1,0
# ]
# L0=[
#     1,1,1,1,1,1,1,1,
#     1,0,1,1,1,0,0,0,
#     0,1,1,1,0,1,1,0,
#     0,1,0,1,0,1,1,1
# ]
# hasil_xor=xor(E_R0,K1)
# print("Hasil XOR: ",hasil_xor)
# result=split_6bit(hasil_xor)
# B1=[]
# for i in range(8):
#     output = sbox(result[i], i + 1)
#     B1.extend(output)
# print("B1",B1)
# pbox_res=pbox(B1)
# print("PBOX:",pbox_res)
# new_R1=xor(pbox_res,L0)