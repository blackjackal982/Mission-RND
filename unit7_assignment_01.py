__author__ = 'Kalyan'

problem = """
 We are going to revisit unit6 assignment3 for this problem.

 Given an input file of words (mixed case). Group those words into anagram groups and write them
 into the destination file so that words in larger anagram groups come before words in smaller anagram sets.

 With in an anagram group, order them in case insensitive ascending sorting order.

 If 2 anagram groups have same count, then set with smaller starting word comes first.

 For e.g. if source contains (ant, Tan, cat, TAC, Act, bat, Tab), the anagram groups are (ant, Tan), (bat, Tab)
 and (Act, cat, TAC) and destination should contain Act, cat, TAC, ant, Tan, bat, Tab (one word in each line).
 the (ant, Tan) set comes before (bat, Tab) as ant < bat.

 At first sight, this looks like a big problem, but you can decompose into smaller problems and crack each one.

 This program should be written as a command line script. It takes one argument the input file of words and outputs
 <input>-results.txt where <input>.txt is the input file of words.
"""
import sys
from collections import defaultdict

def read_words(words_file):
    f = open(words_file,'r')
    data = []
    for i in f.readlines():
        if "#" not in i:
            data+=[word for word in i.split()]
    f.close()
    return data

def anagram_sort(source):
    destination = "unit6_testinput_03-results.txt"
    data = read_words(source)
    data_dict = defaultdict(list)
    for i in data:
        dict_key = "".join(sorted(list(i.replace(" ", "").lower())))
        data_dict[dict_key].append(i)
    res = list(data_dict.values())
    res.sort(key=lambda x: len(x), reverse=True)
    for i in res:
        i.sort(key=lambda x: x.lower())
    res.sort(key=lambda x: x[0].lower())
    res.sort(key=lambda x: len(x), reverse=True)
    f = open(destination, "w")
    for i in res:
        for j in i:
            f.write(j + '\n')
    f.close()

def main(argv = None):
    if argv is None:
        argv = sys.argv
        try:
            try:
                input_file = argv[1]
            except IndexError:
                raise IndexError
            return anagram_sort(input_file)
        except Exception as error:
            print(error,file = sys.stderr)
            return 1

if __name__ == "__main__":
    sys.exit(main())