import MapReduce
import sys

"""
Sparse matrix multiplication in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

def mapper(record):
    # key: position of the element
    # value: element of the matrix
    key = (record[1], record[2])
    value = record[3]
    if record[0] == "a":
        for k in range(5):
            mr.emit_intermediate((key[0],k), (value, key[1]))
    else:
        for j in range(5):
            mr.emit_intermediate((j,key[1]), (value, key[0]))


def reducer(key, list_of_values):
    # key: position in the result matrix
    # value: list of values to add + corresponding column (A) or
    # row (B) number
    total = 0
    p = 0
    for v in list_of_values:
        for w in list_of_values[p+1:]:
            if v[1] == w[1]:
                total += v[0] * w[0]
        p += 1

    mr.emit((key[0], key[1], total))


if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
