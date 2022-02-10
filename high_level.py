#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    word1, word2 = input("Enter the two words: ").split()
    for ch in word1:
        if ch in word2:
            print("Да ", end=" ")
        else:
            print("Нет ", end=" ")
