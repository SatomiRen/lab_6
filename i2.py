#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    word1, word2 = input("Enter the two words: ").split()
    if word1 == word2:
        print("All of the characters from these words are the same!")
        exit(0)
    else:
        n = 0
        for i in range(len(word1)):
            if word1[i] in word2[i]:
                n += 1
            else:
                break
    print(f"There are {n} of the same first letters in these two words")
