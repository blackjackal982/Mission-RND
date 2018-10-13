__author__ = 'Kalyan'

max_marks = 30

problem_notes = '''
This problem is the reverse of problem3. Given the jumbled text created 
according to the rules given in problem 3 and number of steps, create the original text.

Notes:
1. Raise ValueError if n <= 0
2. Raise TypeError if text is not a str
3. Do not search for mathematical patterns, solve this programatically
'''
def gen(n):
    flag = 0
    i = n
    while True:
        if flag == 0:
            yield(i)
            i = i-1
        if flag == 1:
            yield(i)
            i = i+1
        if i == n:
            yield(i)
            flag = 0
        if i == 0:
            yield(i)
            flag = 1

def isListEmpty(inList):
    if isinstance(inList, list): # Is a list
        return all( map(isListEmpty, inList) )
    return False

def unjumble(jumbled_text, n):
    if type(jumbled_text).__name__!="str":
        raise TypeError
    if n<=0:
        raise ValueError
    li_text = list(jumbled_text)
    new = []
    for i in range(n):
         new.append([])
    #repeating steps
    dict_rep = {}
    for i in range(1,n+1):
        dict_rep[i]=0
    i = 0
    Gen = gen(n)
    while i<len(jumbled_text):
         a = next(Gen)
         if a!=0:
            dict_rep[a]+=1
         i = i+a
    for i in range(1,n+1):
         rep = dict_rep[i]
         for j in range(rep):
             if li_text[0:i]:
                new[i-1].append("".join(li_text[0:i]))
                li_text = li_text[i:]
    decrypt = ""
    new_gen_ins = gen(n)
    while True:
        a = next(new_gen_ins)
        if a !=0:
            decrypt += new[a-1][0]
            new[a-1].pop(0)
            if isListEmpty(new):
                break
    return decrypt

def test_unjumble():
    assert "Ashokan" == unjumble("hoAskan", 2)
    # print(unjumble("envekuPramar",3))
    assert unjumble("envekuPramar",3) == "Praveenkumar"
    assert unjumble("nkespo",3) == "spoken"