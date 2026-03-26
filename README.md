# Bioinformatics Toolkit
A simple Python command-line tool for basic bioinformatics tasks.

### Features

- Reverse complement of DNA sequences  
- Global sequence alignment using dynamic programming (BLOSUM62)  
- Input validation for DNA and protein sequences  
- Interactive command-line interface  

### Usage

When running the program, the user can choose between available tasks:

```
Bioinformatics Toolkit
Available tasks:
1 - reverse complement (DNA only: A, C, G, T)
2 - sequence alignment (protein sequences)
```

### Example – Reverse complement

Input:
```
1
ATAC
```

Output:
```
GTAT
```

### Example – Sequence alignment

Input:
```
2
PLEASANTLY
MEANLY
```

Output:
```
8
PLEASANTLY
-MEA--N-LY
```

### Description

This project combines multiple bioinformatics algorithms into a single Python tool.  
It includes string manipulation for DNA processing and a dynamic programming implementation for optimal sequence alignment using the BLOSUM62 scoring matrix.

The alignment algorithm constructs a scoring matrix and reconstructs the optimal alignment through backtracking.

### Technologies

- Python  
- Dynamic programming  
- Basic bioinformatics algorithms  

### Notes

- DNA input is restricted to characters A, C, G, T  
- Protein sequences must contain only standard amino acid letters  
