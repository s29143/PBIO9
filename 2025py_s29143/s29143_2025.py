import random
from argparse import ArgumentError
from random import choice


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

    cg_at_ratio = ((c_count + g_count) / total) * 100

    return {
        'A': percentage_a,
        'C': percentage_c,
        'G': percentage_g,
        'T': percentage_t,
        '%CG': cg_at_ratio
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

# ORIGINAL:
# def main():
# MODIFIED (Wydzielenie generowania jako osobna funkcja na rzecz możliwości wczytywania pliku do analizy)
def generate():
    # ORIGINAL: bez zmian
    # MODIFIED dodano walidacje
    # Pobieranie danych od użytkownika
    length = int(input("Podaj długość sekwencji: "))
    # Walidacja długości
    if length <= 0:
        raise ArgumentError('Długość nie może być zero lub mniej')
    sequence_id = input("Podaj ID sekwencji: ")
    # Walidacja ID
    if sequence_id.strip() == '':
        raise ArgumentError('ID nie może być pusta')
    description = input("Podaj opis sekwencji: ")
    # Walidacja Opisu
    if description.strip() == '':
        raise ArgumentError('Opis nie może być pusty')
    name = input('Podaj imię: ')
    # Walidacja imienia
    if name.strip() == '':
        raise ArgumentError('Imie nie może być puste')

    # ORIGINAL bez zmian
    # MODIFIED dodano wielokrotne generowanie
    choice = ''
    while choice != 'n':
        # Generowanie losowej sekwencji DNA
        dna_sequence = generate_dna_sequence(length)
        print(f'Wygenerowano sekwencje {dna_sequence}')
        # Wybór użytkownika
        choice = input('Wygenerować ponownie? (y/n): ')

    # Obliczanie statystyk
    stats = calculate_statistics(dna_sequence)

    # Wstawianie imienia do sekwencji
    dna_with_name = insert_name(dna_sequence, name)

    # Wyświetlanie statystyk
    print("\nStatystyki sekwencji:")
    for key, value in stats.items():
        print(f"{key}: {value:.2f}%")

    # Zapis do pliku FASTA
    save_to_fasta(dna_with_name, sequence_id, description)
    print(f"\nSekwencja została zapisana do pliku {sequence_id}.fasta")

# Dodano funkcję analyze
def analyze():
    file_name = input("Podaj nazwę pliku fasta: ")
    name = input('Podaj imię w sekwencji: ')
    # Otwarcie pliku podanego przez użytkownika
    with open(file_name, "r") as fasta_file:
        # Odczytanie pierwszej linii by odczytać ID i opis
        header = fasta_file.readline()
        # Odczytanie sekwencji
        sequence = fasta_file.readline()
        # Sprawdzenie czy imie jest w sekwencji
        if name not in sequence:
            raise ArgumentError('Nie znaleziono imienia w sekwencji')
        # Usunięcie imienia z sekwencji
        sequence = sequence.replace(name, '')
        print(f'Wczytano sekwencję o ID: {header.split(' ')[0][1:]} opis: {header.split(' ')[1]}\n')
        print(f'Długość sekwencji {len(sequence)}')
        # Wyliczenie statystyk dla wczytanej sekwencji
        stats = calculate_statistics(sequence)
        for key, value in stats.items():
            print(f"{key}: {value:.2f}%")

def main():
    # Wczytanie wyboru od użytkownika
    choice = int(input('1. Generowanie sekwencji.\n2. Analiza sekwencji\n'))
    if choice == 1:
        generate()
    elif choice == 2:
        analyze()
if __name__ == "__main__":
    main()
