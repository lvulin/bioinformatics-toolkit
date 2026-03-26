import argparse

def reverse_complement(dna):
    complement = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }
    return "".join(complement[x] for x in dna[::-1])


def main():
    parser = argparse.ArgumentParser(description="Bioinformatics Toolkit")
    
    parser.add_argument("--task", required=True, help="Task: reverse")
    parser.add_argument("--seq1", required=True, help="DNA sequence")

    args = parser.parse_args()

    if args.task == "reverse":
        result = reverse_complement(args.seq1)
        print(result)

    else:
        print("Unknown task")


if __name__ == "__main__":
    main()
