import random


def generate_dna_sequence(length):
    """Generuje losową sekwencję DNA z liter A, C, G, T."""
    nucleotides = ['A', 'C', 'G', 'T']
    return ''.join(random.choice(nucleotides) for _ in range(length))


def calculate_statistics(sequence):
    """Oblicza statystyki sekwencji DNA."""
    a_count = sequence.count('A')
    c_count = sequence.count('C')
    g_count = sequence.count('G')
    t_count = sequence.count('T')

    total = len(sequence)
    percentage_a = (a_count / total) * 100
    percentage_c = (c_count / total) * 100
    percentage_g = (g_count / total) * 100
    percentage_t = (t_count / total) * 100

    cg_at_ratio = (c_count + g_count) / (a_count + t_count) if (a_count + t_count) != 0 else 0

    return {
        'A': percentage_a,
        'C': percentage_c,
        'G': percentage_g,
        'T': percentage_t,
        'CG/AT Ratio': cg_at_ratio
    }


def insert_name(sequence, name):
    """Wstawia imię w losowe miejsce w sekwencji, nie wpływając na długość sekwencji."""
    index = random.randint(0, len(sequence) - 1)
    return sequence[:index] + name + sequence[index:]


def save_to_fasta(sequence, sequence_id, description):
    """Zapisuje sekwencję DNA w formacie FASTA do pliku."""
    with open(f"{sequence_id}.fasta", "w") as fasta_file:
        fasta_file.write(f">{sequence_id} {description}\n")
        fasta_file.write(sequence)


def main():
    # Pobieranie danych od użytkownika
    length = int(input("Podaj długość sekwencji: "))
    sequence_id = input("Podaj ID sekwencji: ")
    description = input("Podaj opis sekwencji: ")
    name = input('Podaj imię: ')

    # Generowanie losowej sekwencji DNA
    dna_sequence = generate_dna_sequence(length)

    # Wstawianie imienia do sekwencji
    dna_with_name = insert_name(dna_sequence, name)

    # Obliczanie statystyk
    stats = calculate_statistics(dna_with_name)

    # Wyświetlanie statystyk
    print("\nStatystyki sekwencji:")
    for key, value in stats.items():
        print(f"{key}: {value:.2f}%")

    # Zapis do pliku FASTA
    save_to_fasta(dna_with_name, sequence_id, description)
    print(f"\nSekwencja została zapisana do pliku {sequence_id}.fasta")


if __name__ == "__main__":
    main()
