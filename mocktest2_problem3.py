__author__ = 'Kalyan'

max_marks = 25

problem_notes = '''
Given a sentence transform all words in it according to
the following guidelines:

1. Move all vowels before all the consonents
2. Maintain relative ordering among the vowels and consonents.
3. If two equal letters come next to each other (case insensitive duplicates), drop the second letter
4. Preserve the case of the original letters.
5. Words are separated by spaces. Drop all non-letters like digits and punctuation and special chars in the sentence.

For e.g eagle becomes eaegl, ApPle become Aepl(repeating P dropped)

Write helper sub routines as required
'''
# do type checking, non-str should raise TypeException
import string
valid_words = string.ascii_uppercase+string.ascii_lowercase

def remove_adjacent(let):
  i = 1
  while i < len(let):
    if let[i].lower() == let[i-1].lower():
      let.pop(i)
      i -= 1
    i += 1
  return let

def transform(sentence):
    if type(sentence).__name__!='str':
        raise TypeError
    vowels = "aeiou"
    sentence = sentence.split(" ")
    list_word = []
    for i in sentence:
        i = tuple(list(i))
        list_word.append(i)
    res = []
    for i in list_word:
        v = []
        c= []
        for j in i:
            if j in valid_words:
                if j.lower() in vowels:
                    v.append(j)
                else:
                    c.append(j)
        res.append((v+c))
    final_word = ""
    res =[remove_adjacent(i) for i in res]
    for i in res:
        final_word=final_word+"".join(i)+" "
    return final_word.strip()

def test_transform():
    assert "Aepl eaegl and ES" == transform("Apple, eagle and SE00e")
    assert TypeError,transform("")
    assert "eohl owrld" == transform("hello world")
    assert TypeError,transform(20)
    assert transform("education")=="euaiodctn"
    assert transform("hey there! wassup") == "ehy ethr auwsp"
    assert transform("hey 123hyie")=="ehy iehy"
    assert transform("hello big bang theory")== "eohl ibg abng eothry"
    assert transform("heeeeeeeeeehe") == "eh"
    assert transform("heHHHHHHHeeeeeeee") == "eh"
    assert transform("Badass fellow") == "aBds eoflw"
    assert transform("sea she her")=="eas esh ehr"