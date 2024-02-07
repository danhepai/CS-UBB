# Găsiți sublista cea mai lunga cu numere de maxim 2 cifre crescătoare. Folosiți programare dinamică,
# se cere recurența
# si implementare iterativă în Python.
# Ex: Pentru lista [22, 2, 11, 13, 10, 4, 5, 7, 15, 9, 11, 8] soluția este 2, 4, 8 (2p)

def longest_subsequence(arr):
    for k in range(len(arr) - 1, -1, -1):
        if arr[k] % 100 == arr[k]:
            arr = arr[:k + 1]
            break

    max_lengths = [0] * len(arr)
    indexes = [0] * len(arr)
    max_lengths[-1] = 1
    indexes[-1] = -1

    for k in range(len(arr) - 2, -1, -1):
        if arr[k] % 100 == arr[k]:
            indexes[k] = -1
            max_lengths[k] = 1
            for i in range(k + 1, len(arr)):
                if arr[k] <= arr[i] and max_lengths[k] < max_lengths[i] + 1:
                    max_lengths[k] = max_lengths[i] + 1
                    indexes[k] = i

    starting_point = 0
    for i in range(0, len(arr)):
        if max_lengths[i] > max_lengths[starting_point]:
            starting_point = i

    answer = []
    current_index = starting_point
    while current_index != -1:
        answer.append(arr[current_index])
        starting_point = indexes[current_index]

    print(answer)


def longest_subsequence_with_even_decresing_nums(arr):
    for el in range(len(arr) - 1, -1, -1):
        if arr[el] % 2 == 0:
            arr = arr[:el + 1]
            break

    max_lengths = [0] * len(arr)
    max_lengths[-1] = 1
    indexes = [0] * len(arr)
    indexes[-1] = -1

    for current_ind in range(len(arr) - 2, -1, -1):
        if arr[current_ind] % 2 == 0:
            max_lengths[current_ind] = 1
            indexes[current_ind] = -1

            for possible_ind in range(current_ind + 1, len(arr)):
                if arr[current_ind] >= arr[possible_ind] and max_lengths[current_ind] < max_lengths[possible_ind] + 1:
                    max_lengths[current_ind] = max_lengths[possible_ind] + 1
                    indexes[current_ind] = possible_ind

    starting_point = 0
    for i in range(0, len(arr)):
        if max_lengths[i] > max_lengths[starting_point]:
            starting_point = i

    current_point = starting_point
    answer = []
    while current_point != -1:
        answer.append(arr[current_point])
        current_point = indexes[current_point]

    print(answer)

    # Imi aduc ultimul element bun pe ultima pozitie. Iau doi vectori, de lungime maxima([-1] = 1) si de indexi([-1] = -1).
    # plec invers de la pen-ultimu. daca elementu ii bun: seteaza-i max len la 1 si indexu la -1. dupa
    # mergi normal si daca gasesti un element care are len + 1 mai mare si satisface conditia
    # pune-i max len la max_len + 1 si seteaza-i indexu la el.
    #
    # gaseste starting point(ala cu lungimea maxima)
    # cat timp n-ai ajuns pe final(-1), adauga elementul in lista answer si mergi pe urmatoarea pozitie




longest_subsequence_with_even_decresing_nums([2, 12, 3, 6, 14, 3, 4, 7, 2])