#!/usr/bin/env python3

def return_evens(num_list):
    return[ n for n in num_list if n % 2 == 0]

def make_exclamation(sentence_list):
    return[ x + '!' for x in sentence_list ]
    