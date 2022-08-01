import itertools
import sys


def find_all_n_letter_words(letter_sequence, dict, n):
    # Get every combination of n letters in letter sequence
    letter_combos = itertools.combinations(letter_sequence, n)
    solutions = set()

    for letter_combo in letter_combos:
        # Create list of all permuations of the letter combination
        perms = [''.join(p) for p in itertools.permutations(letter_combo)]
        # Get all permutations that are valid words
        valid_words = set(dict).intersection(perms)

        solutions = solutions.union(valid_words)

    return solutions


def find_all_words(letter_sequence, dict):
    print("Entered letter sequence:", letter_sequence)
    print("Finding all words that can be constructed from these letters...\n")

    for n in range(1, len(letter_sequence) + 1):
        solutions = find_all_n_letter_words(letter_sequence, dict, n)

        print("%i letters:" %n)

        if(len(solutions) > 0):
            print("%i valid dictionary words found:" %len(solutions))
            print(sorted(solutions))
        else:
            print("No valid dictionary words found...")
        print("\n")



# Open sorted dictionary with max 9 letter words
with open('sortedDic.txt', 'r') as fileopen:
    sorted_eng_dict = [line.strip() for line in fileopen]

find_all_words(str(sys.argv[1]), sorted_eng_dict)

