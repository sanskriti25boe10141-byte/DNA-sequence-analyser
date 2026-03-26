print("=== DNA Sequence Analyzer ===")

def get_dna_sequence():
    seq = input("Enter your DNA sequence: ").upper()
    return seq


def validate_sequence(seq):
    valid_bases = "ATGC"
    for base in seq:
        if base not in valid_bases:
            return False
    return True


def count_nucleotides(seq):
    counts = {
        "A": 0,
        "T": 0,
        "G": 0,
        "C": 0
    }

    for base in seq:
        counts[base] += 1

    return counts


def calculate_gc_content(seq):
    g = seq.count("G")
    c = seq.count("C")
    gc = ((g + c) / len(seq)) * 100
    return round(gc, 2)


def reverse_complement(seq):
    complement = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }

    reversed_seq = seq[::-1]
    result = ""

    for base in reversed_seq:
        result += complement[base]

    return result


# Main Program
dna = get_dna_sequence()

if validate_sequence(dna):
    print("\nValid DNA sequence ✅")

    counts = count_nucleotides(dna)
    print("Nucleotide Count:", counts)

    gc_content = calculate_gc_content(dna)
    print("GC Content:", gc_content, "%")

    rev_comp = reverse_complement(dna)
    print("Reverse Complement:", rev_comp)

else:
    print("\nInvalid DNA sequence ❌ (Only A, T, G, C allowed)")