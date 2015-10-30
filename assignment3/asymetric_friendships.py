import MapReduce
import sys

"""
Finding asymetric friendships in the Simple Python MapReduce Framework
Returns a list of name where Person 1 is friend whith Person 2, but
Person 2 isn't friend with Person 1
"""

mr = MapReduce.MapReduce()


def mapper(record):
    # key: string PersonAPersonB (alphabetical order)
    # value : (PersonA, PersonB) pair
    key = sorted(record)[0] + sorted(record)[1]
    value = record
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: string PersonAPersonB (alphabetical order)
    # value: (PersonA, PersonB) pair

    # If a friendship is seen only once, it's means asymetric
    # relationship. The pairs (PersonA, PersonB) and
    # (PersonB, PersonA) are returned.
    if len(list_of_values) == 1:
        mr.emit((tuple(sorted(list_of_values[0]))))
        mr.emit((tuple(sorted(list_of_values[0],reverse=True))))



if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
