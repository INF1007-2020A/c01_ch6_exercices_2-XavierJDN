#!/usr/bin/env python
# -*- coding: utf-8 -*-


from matplotlib.colors import cnames


def list_to_dict(some_list: list) -> dict:
    # TODO: Transformer la liste en dictionnaire, les éléments de la liste deviennent les clés et leur index deviennent les valeurs
    some_dict = {}
    for index, element in enumerate(some_list):
        some_dict[element] = index

    return some_dict


def color_name_to_hex(colors: list) -> list:
    return [(color, cnames[color]) for color in colors]
    # TODO: Trouver la valeur hex de chaque couleur dans la liste et créer une liste de tupple où le premier élément est le nom de la couleur et le deuxième est la valeur hex


def odd_integer_for_loop(end: int) -> list:
    list_odd = []
    for number in range(0, end):
        if number % 2 != 0:
            list_odd.append(number)
    return list_odd


def odd_integer_list_comprehension(end: int) -> list:
    return [number for number in range(0, end) if number % 2 != 0]


def loop_traversal(integers: list) -> None:
    for index, element in enumerate(integers):
        print(index, element)


def word_dict_for_loop(words: list) -> dict:
    words_dict = {}
    for word in words:
        words_dict[word[:3].upper()] = word
    return words_dict


def word_dict_comprehension(words: list) -> dict:
    return {word[:3].upper(): word for word in words}


def dictionary_traversal(words: dict) -> None:
    for k, v in words.items():
        print(k, v)


def main() -> None:
    some_list = ["a", "b", "z", "patate"]
    print(f"La liste suivante {some_list} est transformée en dictionnaire: {list_to_dict(some_list)}")

    colors = ["blue", "red", "green", "yellow", "black", "white"]
    print(f"La valeur hex associée aux couleurs est: {color_name_to_hex(colors)}")

    integer = 13
    integers_for = odd_integer_for_loop(integer)
    print(f"Liste avec boucle for et le nombre 13: {integers_for}")
    integers_comprehension = odd_integer_for_loop(integer)
    print(f"Liste avec list comprehension et le nombre 13: {integers_comprehension}")

    print(f"Les 2 listes sont-elles identiques? {integers_for == integers_comprehension}")
    print(f"Parcours d'une des 2 listes...")
    loop_traversal(integers_for)

    words = ["initialisation", "ajout", "modification", "suppression", "dictionnaire"]
    words_for = word_dict_for_loop(words)
    print(f"Dictionnaire avec la boucle for: {words_for}")
    words_comprehension = word_dict_comprehension(words)
    print(f"Dictionnaire avec le dictionary comprehension: {words_comprehension}")

    print(f"Les 2 dictionnaires sont-ils identiques? {words_for == words_comprehension}")
    print(f"Parcours d'un des 2 dictionnaires...")
    dictionary_traversal(words_comprehension)


if __name__ == '__main__':
    main()
