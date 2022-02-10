#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    sentence = input("Enter the sentence: ")
    sentence = sentence.replace('c', '')  # Удаление английских букв "с"
    sentence = sentence.replace('с', '')  # Удаление русских букв "с"
    print(sentence)
