import MapReduce
import sys

"""
Trimming the last 10 character of a string of nucleotide
and removing the duplicates in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()


def mapper(record):
    # key: sequence id
    # value: sequence
    key = record[0]
    value = record[1]
    mr.emit_intermediate(value[:-10], 1)

def reducer(key, list_of_values):
    # key: trimmed sequence
    # value: list of occurrence counts
    mr.emit((key))

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
