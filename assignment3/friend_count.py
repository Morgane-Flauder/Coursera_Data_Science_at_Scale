import MapReduce
import sys

"""
Counting friends in a social network dataset in the Simple Python
MapReduce Framework
"""

mr = MapReduce.MapReduce()


def mapper(record):
    # key: personA
    key = record[0]
    mr.emit_intermediate(key, 1)

def reducer(key, list_of_values):
    # key: personA
    # value: list of friends counts
    total = 0
    for f in list_of_values:
        total += f
    mr.emit((key, total))


if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
