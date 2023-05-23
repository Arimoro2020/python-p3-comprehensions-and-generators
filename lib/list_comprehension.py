#!/usr/bin/env python3

def return_evens(num_list):
    even_list = [x for x in num_list if x % 2 == 0]
    return even_list



def make_exclamation(sentence_list):
    sentence_list = [ string + "!" for string  in sentence_list]
    return sentence_list