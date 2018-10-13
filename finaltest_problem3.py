__author__ = 'Kalyan'

max_marks = 25

problem_notes = '''
For this problem you have to implement a staircase jumble as described below. 

1. You have n stairs numbered 1 to n. You are given some text to jumble.
2. You repeatedly climb down and up the stairs and on each step k you add/append starting k chars from 
   the text you have (and remove them from the text). 
3. You repeat this process till you finish the whole text.
4. Finally you climb up from step 1 and collect all chars to get the jumbled text.

E.g.  if the text is "Ashokan" and n = 2.  You have the following text on the steps. First you drop 

 "As" on step 2, then "h" on step 1, then you get to the ground and you 
 climb back again droping "o" on step 1 and "ka" on step2 and finally "n" on step2 
 (since you have run out of chars and you dont have 2 chars).
  
 So sequence of steps is 2, 1 then 1, 2 then 2, 1 and so on...
 
(step2)As;ka;n
       ----
   (step 1)|h;o
           ----
Final jumbled text is hoAskan (all text on step1 followed by all text on step2, the ; is shown above only to visually 
distinguish the segments of text dropped on the stair at different times)

Notes:
1. Raise ValueError if n <= 0
2. Raise TypeError if text is not a str
3. Note that spaces, punctuation or any other chars are all treated like regular chars and 
   they will be jumbled in same way.
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

def jumble(text, n):
    if n<=0:
        raise ValueError
    if type(text).__name__!="str" or text == "":
        raise TypeError
    li_text = list(text)
    Gen = gen(n)
    new = []
    for i in range(n):
        new.append([])
    while len(li_text)>0:
        val = next(Gen)
        if val!=0:
            chars = li_text[0:val]
            new[val-1].append("".join(chars))
            for i in chars:
                li_text.remove(i)
    mod = ""
    for i in new:
        mod += "".join(i)
    return mod

def test_jumble():
    assert "hoAskan" == jumble("Ashokan", 2)
    assert "h;Ask n" == jumble("Ash;k n",2)
    assert jumble("Armybattle",3) == "atybtlArme"
    assert jumble("Batsman",4) =="manBats"
    assert jumble("PraveenKumar",3) == "enveKuPramar"
    try:
        jumble("",0)
    except ValueError:
        pass
    try:
        jumble("hashika",0)
    except ValueError:
        pass