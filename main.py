import argparse

def reverse_complement(dna):
    complement = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }
    return "".join(complement[x] for x in dna[::-1])

#BA5E
def alignRecontructionMoves(backtrack):
    n = len(backtrack) - 1
    m = len(backtrack[0]) - 1
    moves = []
    while n > 0 or m > 0:
        moves.append(backtrack[n][m])
        if backtrack[n][m] == "D":
            n = n - 1
        elif backtrack[n][m] == "R":
            m = m - 1
        else:
            m = m - 1
            n = n - 1

    return moves[::-1]


def moves_to_strings(first_word, second_word, moves):
    pointer_w1 = 0
    pointer_w2 = 0

    w1 = []
    w2 = []

    for move in moves:
        if move == "D":
            w1.append(first_word[pointer_w1])
            pointer_w1 += 1
            w2.append("-")
        if move == "R":
            w1.append("-")
            w2.append(second_word[pointer_w2])
            pointer_w2 += 1
        if move == "Diag":
            w1.append(first_word[pointer_w1])
            pointer_w1 += 1
            w2.append(second_word[pointer_w2])
            pointer_w2 += 1

    return "".join(w1), "".join(w2)

def globalalignment(first, second):
    s=[]
    for i in range (len(first)+1):
        s.append([])
    s[0].append(0)
    #first column
    for i in range(1,len(first)+1):
        s[i].append(s[i-1][0]-5)#sigma=5
    #first row
    for j in range(1,len(second)+1):
        s[0].append(s[0][j-1]-5)

    newFirst=""
    newSecond=""

    Backtrack=[]
    for i in range (len(first)+1):
        Backtrack.append([])
    Backtrack[0].append('')
    # first column
    for i in range(1, len(first) + 1):
        Backtrack[i].append("D")
    # first row
    for j in range(1, len(second) + 1):
        Backtrack[0].append("R")

    penality = getPenality()
    index = getInedexOfLetter()
    for i in range(1, len(first) + 1):
        for j in range(1, len(second) + 1):
            s[i].append(
                max(s[i - 1][j] - 5, s[i][j - 1] - 5, s[i - 1][j - 1] + penality[first[i - 1]][index[second[j - 1]]]))

            if s[i][j]==s[i-1][j]-5:
                Backtrack[i].append("D")
            else:
                if s[i][j]==s[i][j-1]-5:
                    Backtrack[i].append("R")
                else:
                    Backtrack[i].append("Diag")

    newFirst,newSecond= moves_to_strings(first,second,alignRecontructionMoves(Backtrack))
    return str(s[len(first)][len(second)])+"\n"+ newFirst+"\n"+newSecond

def getPenality():
    penality={
    "A":[4,  0, -2, -1, -2,  0, -2, -1, -1, -1, -1, -2, -1, -1, -1,  1,  0,  0, -3, -2],
    "C":[0,  9, -3, -4, -2, -3, -3, -1, -3, -1, -1, -3, -3, -3, -3, -1, -1, -1, -2, -2],
    "D":[-2, -3,  6,  2, -3, -1, -1, -3, -1, -4, -3,  1, -1,  0, -2,  0, -1, -3, -4, -3],
    "E":[-1, -4,  2,  5, -3, -2,  0, -3,  1, -3, -2,  0, -1,  2,  0,  0, -1, -2, -3, -2],
    "F":[-2, -2, -3, -3,  6, -3, -1,  0, -3,  0,  0, -3, -4, -3, -3, -2, -2, -1,  1,  3],
    "G":[0, -3, -1, -2, -3,  6, -2, -4, -2, -4, -3,  0, -2, -2, -2,  0, -2, -3, -2, -3],
    "H":[-2, -3, -1,  0, -1, -2,  8, -3, -1, -3, -2,  1, -2,  0,  0, -1, -2, -3, -2,  2],
    "I":[-1, -1, -3, -3,  0, -4, -3,  4, -3,  2,  1, -3, -3, -3, -3, -2, -1,  3, -3, -1],
    "K":[-1, -3, -1,  1, -3, -2, -1, -3,  5, -2, -1,  0, -1,  1,  2,  0, -1, -2, -3, -2],
    "L":[-1, -1, -4, -3,  0, -4, -3,  2, -2,  4,  2, -3, -3, -2, -2, -2, -1,  1, -2, -1],
    "M":[-1, -1, -3, -2,  0, -3, -2,  1, -1,  2,  5, -2, -2,  0, -1, -1, -1,  1, -1, -1],
    "N":[-2, -3,  1,  0, -3,  0,  1, -3,  0, -3, -2,  6, -2,  0,  0,  1,  0, -3, -4, -2],
    "P":[-1, -3, -1, -1, -4, -2, -2, -3, -1, -3, -2, -2,  7, -1, -2, -1, -1, -2, -4, -3],
    "Q":[-1, -3,  0,  2, -3, -2,  0, -3,  1, -2,  0,  0, -1,  5,  1,  0, -1, -2, -2, -1],
    "R":[-1, -3, -2,  0, -3, -2,  0, -3,  2, -2, -1,  0, -2,  1,  5, -1, -1, -3, -3, -2],
    "S":[1, -1,  0,  0, -2,  0, -1, -2,  0, -2, -1,  1, -1,  0, -1,  4,  1, -2, -3, -2],
    "T":[0, -1, -1, -1, -2, -2, -2, -1, -1, -1, -1,  0, -1, -1, -1,  1,  5,  0, -2, -2],
    "V":[0, -1, -3, -2, -1, -3, -3,  3, -2,  1,  1, -3, -2, -2, -3, -2,  0,  4, -3, -1],
    "W":[-3, -2, -4, -3,  1, -2, -2, -3, -3, -2, -1, -4, -4, -2, -3, -3, -2, -3, 11,  2],
    "Y":[-2, -2, -3, -2,  3, -3,  2, -1, -2, -1, -1, -2, -3, -1, -2, -2, -2, -1,  2,  7]
    }
    return penality

def getInedexOfLetter():
    index={
    "A":0,
    "C":1,
    "D":2,
    "E":3,
    "F":4,
    "G":5,
    "H":6,
    "I":7,
    "K":8,
    "L":9,
    "M":10,
    "N":11,
    "P":12,
    "Q":13,
    "R":14,
    "S":15,
    "T":16,
    "V":17,
    "W":18,
    "Y":19
    }
    return index
    
    
     
    inlines = x.split('\n')
    first = inlines[0]
    second = inlines[1]
    res = globalalignment(first, second)
    print(res)
    
def is_valid_dna(seq):
    return all(c in "ACGT" for c in seq)

def is_valid_protein(seq):
    valid_amino_acids = "ACDEFGHIKLMNPQRSTVWY"
    return all(c in valid_amino_acids for c in seq)


print("Bioinformatics Toolkit")
print("Available tasks:")
print("1 - reverse complement (DNA only: A, C, G, T)")
print("2 - sequence alignment (protein sequences)")

while True:
    task = input("Choose task (1 or 2): ")

    if task == "1":
        while True:
            dna = input("Enter DNA sequence (only A, C, G, T): ").upper()

            if is_valid_dna(dna):
                print("Result:")
                print(reverse_complement(dna))
                break
            else:
                print("Invalid DNA sequence. Use only A, C, G, T.\n")

        break

    elif task == "2":
        while True:
            seq1 = input("Enter first sequence (amino acids): ").upper()
            seq2 = input("Enter second sequence (amino acids): ").upper()

            if is_valid_protein(seq1) and is_valid_protein(seq2):
                print("Result:")
                print(globalalignment(seq1, seq2))
                break
            else:
                print("Invalid protein sequence. Use only standard amino acid letters:")
                print("A, C, D, E, F, G, H, I, K, L, M, N, P, Q, R, S, T, V, W, Y\n")

        break

    else:
        print("Invalid choice. Please enter 1 or 2.\n")
