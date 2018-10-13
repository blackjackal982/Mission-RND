__author__ = 'Kalyan'

max_marks = 25

problem_notes = '''
You're given a text file containing names of movie actors and films they've acted in - delimited
by : after actor and movies are separated by commas as described below. movie names may contain : and space
too but not a comma.

Format:
{actor name}: {movie name 1}, {movie name 2}, {movie name 3}

Input:
File containing movies info, a number 'n' which represents the number of lines from top of file and an
actors name.

Output:
For the given actor, you must return all Chemistry records with co-actors that the actor as worked with from the
data in the first n lines.

The records must be sorted by number of movies worked together (descending), in case of a tie, the actors name should be used
for sorting (alphabetical order)

If a given actor has no common movies with any other, then do not emit any chemistry records.

Example:
if a1 and a2 have c1 as common movie
and a1 and a3 have c1, c2, c3 as common movies
and a1 has no common movies with any other actor, then you must return (a3 record, followed by a2 record)


Notes:
1. No special type checking required. raise ValueError if n < 0
2. You must work as if the file has only n lines, so if given actor is not in the first n lines, return empty list.
3. See if you can decompose this problem into meaningful subroutines.
4. Submit the movies.txt file into dropbox too. ** Do not modify the movies.txt file! **
'''

import inspect
import os

# represents the chemistry between two actors and the common movies between them.
# movies is a set of common movies, the actor and co_actor are name strings
class Chemistry(object):
    def __init__(self, actor, co_actor, movies):
        if not actor: raise ValueError("actor is not valid name")
        if not co_actor: raise ValueError("co-actor is not valid name")

        self.actor = actor
        self.co_actor = co_actor
        self.movies = movies

    def __hash__(self):
        return hash(self.actor)

    def __eq__(self, other):
        return (self.actor == other.actor) \
            and (self.co_actor == other.co_actor) \
            and (self.movies == other.movies)

    def __repr__(self):
        return str((self.actor, self.co_actor, self.movies))


# returns a list of Chemistry objects for the given actor sorted by the specified criteria.
# It is as if the file has only first n lines.
# Important: Use the helper routine given (open_input_file) to open the file to open the file which should
# be in same directory as this file.
def get_chemistry(input_file, n, actor):
    file = open_input_file(input_file)
    count = 0
    acted = {}
    for line in file.readlines():
        try:
            key= (line.strip().split(":"))[0].strip()
            val = (line.strip().split(":"))[1].strip()
            a = [v.strip() for v in val.split(",")]
            acted[key]=a
            count = count+1
            if count == n:
                break
        except IndexError:
            pass
    l = []
    for i in acted:
        if i != actor:
            if set(acted[i])&set(acted[actor]):
                l.append(Chemistry(actor,i,set(acted[i])&set(acted[actor])))
    l.sort(key = lambda x:x.actor)
    l.sort(key = lambda x:len(x.movies),reverse=True)
    return l

def test_actors_chemistry():
    assert [Chemistry('Leonardo Di Caprio', 'Tom Hardy', {'Inception', 'The Revenant'})]\
           == get_chemistry('movies.txt', 4, "Leonardo Di Caprio")

def get_module_dir():
    mod_file = inspect.getfile(inspect.currentframe())
    mod_dir = os.path.dirname(mod_file)
    return mod_dir


def open_input_file(file, mode="rt"):
    mod_dir = get_module_dir()
    test_file = os.path.join(mod_dir, file)
    return open(test_file, mode)
