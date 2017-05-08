#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Übung 5 Aufgabe 1
# Valentina Vogel & Martina Stüssi
# Minimale Editierdistanz berechnen zwischen zwei tokenisierten Sätzen.
# Wortalignierung und Operationen ebenfalls ausgeben.

def main():
    levenshtein_backtraced()

def levenshtein_backtraced():
    source_a = ['This', 'is', 'nice', 'cat', 'food', '.']
    target_a = ['this', 'is', 'the', 'nice', 'cat', '.']

    source_b = ['The', 'cat', 'likes', 'tasty', 'fish', '.']
    target_b = ['The', 'cat', 'likes', 'fish', 'very', 'much', '.']

    source_c = ['I', 'have', 'adopted', 'cute', 'cats', '.']
    target_c = ['I', 'have', 'many', 'cats', '.']

    x = levenshtein_distance(source_a, target_a)
    y = levenshtein_distance(source_b, target_b)
    z = levenshtein_distance(source_c, target_c)

    print_it(x)
    print_it(y)
    print_it(z)

def levenshtein_distance(source, target):
    n = len(source)
    m = len(target)
    d =[[None for _ in range(m+1)] for _ in range(n+1)]
    d[0][0] = 0
    for i in range(1, n+1):
        d[i][0] = d[i-1][0] + 1
    for j in range (1, m+1):
        d[0][j] = d[0][j-1] + 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            d[i][j] = min(
                d[i-1][j] + 1, #del
                d[i][j-1] + 1, #insert
                d[i-1][j-1] + (1 if source[i-1] != target[j-1] else 0)#sub/same
                )
    list_op = []
    list_in = []
    list_out = []
    for _ in range(0, n+1):
        for _ in range(0, m+1):
            if i>0 and j>0 and d[i-1][j] + 1 == d[i][j]: #delete
                list_op.append('D')
                list_in.append(source[i-1])
                list_out.append('*')
                i = i-1

            elif i>0 and j>0 and d[i][j-1] + 1 == d[i][j]: #insert
                list_op.append('I')
                list_in.append('*')
                list_out.append(target[j-1])
                j = j-1

            elif i>0 and j>0 and d[i-1][j-1] == d[i][j]: #diagonal
                list_op.append(' ')
                list_in.append(source[i-1])
                list_out.append(target[j-1])
                i = i-1
                j = j-1

            elif i>0 and j>0 and d[i-1][j-1] + 1 == d[i][j]: #diagonal
                list_op.append('S')
                list_in.append(source[i-1])
                list_out.append(target[j-1])
                i = i-1
                j = j-1
    list_in.reverse()
    list_out.reverse()
    list_op.reverse()
    return (list_in, list_out, list_op, d[n][m])

def list_to_string(uglylist):
    schoeneliste = []
    for i in uglylist:
        j = ("{:7}".format(i))
        schoeneliste.append(j)
    schoenerstring = ' '.join(schoeneliste)
    return schoenerstring

def print_it(list):
    print(list_to_string(list[0]))
    print(list_to_string(len(list[0]) * '|'))
    print(list_to_string(list[1]))
    print(list_to_string(list[2]))
    print('Editierdistanz:', list[3], '\n')

if __name__ == '__main__':
        main()

# http://stacioverflow.com/questions/529424/traverse-a-list-in-reverse-order-in-python
# http://stacioverflow.com/questions/7286365/print-a-list-in-reverse-order-with-range
# http://stacioverflow.com/questions/14228884/show-string-alignment
