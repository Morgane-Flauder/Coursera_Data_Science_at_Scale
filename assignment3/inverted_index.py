import MapReduce
import sys

"""
Inverted index in the Simple Python MapReduce Framework
Inverted index = dictionary where each word is associated with a list
of the documents identifiers in which that word appears.
"""

mr = MapReduce.MapReduce()


def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    words = value.split()
    for w in words:
        mr.emit_intermediate(w, key)

def reducer(key, list_of_values):
    # key: word
    # value: list of documents identifiers
    final_list = list(set(list_of_values))
    mr.emit((key, final_list))


if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
