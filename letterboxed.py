from copy import deepcopy
import itertools

def solutions(a, b, c, d):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letters = a + b + c + d
    bad_letters = [letter for letter in alphabet if letter not in letters]
    potential_words = set()
    potential_solutions = set()
    with open('words.txt') as wordfile:
        for potential_word in wordfile.read().splitlines():
            if not any(letter in potential_word for letter in bad_letters):
                potential_words.add(potential_word)
                words = deepcopy(potential_words)
    for word in potential_words:
        if any((set(word[i:i+2]).issubset(set(a)) for i in range(len(word) - 1))):
            words.remove(word)
            continue
        if any((set(word[i:i+2]).issubset(set(b)) for i in range(len(word) - 1))):
            words.remove(word)
            continue
        if any((set(word[i:i+2]).issubset(set(c)) for i in range(len(word) - 1))):
            words.remove(word)
            continue
        if any((set(word[i:i+2]).issubset(set(d)) for i in range(len(word) - 1))):
            words.remove(word)
            continue
    for word in words:
        if all(letter in (list(word)) for letter in letters):
            potential_solutions.add(word)
            num_words = 1
    if not len(potential_solutions):
        for pair in list(itertools.combinations(words, 2)):
            if all(letter in (list(pair[0]) + list(pair[1])) for letter in letters) and list(pair[0])[-1] == list(pair[1])[0]:
                potential_solutions.add(pair)
                num_words = 2
    if not len(potential_solutions):
        for trio in list(itertools.combinations(words, 3)):
            if all(letter in (list(trio[0]) + list(trio[1]) + list(trio[2])) for letter in letters) and list(trio[0])[-1] == list(trio[1])[0] and list(trio[1])[-1] == list(trio[2])[0]:
                potential_solutions.add(trio)
                num_words = 3
                break
    if not len(potential_solutions):
        print('This LetterBoxed has no 1, 2, or 3 word solutions.')
    if len(potential_solutions) > 1:
        yes_or_no = input(f'This LetterBoxed has multiple solutions with {num_words} word(s). Would you like to know them? Y/N: ')
    if len(potential_solutions) == 1:
        yes_or_no = input(f'This LetterBoxed has a solution with {num_words} word(s). Would you like to know it? Y/N: ')
    print(potential_solutions) if yes_or_no.upper() == 'Y' else print('Okay!')

list1 = input("First set of letters: ")
list2 = input("Second set of letters: ")
list3 = input("Third set of letters: ")
list4 = input("Fourth set of letters: ")
solutions(list1, list2, list3, list4)
