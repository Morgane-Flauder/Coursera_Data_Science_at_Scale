import MapReduce
import sys

"""
Relational join in the Simple Python MapReduce Framework
It correspond to the following SQL query :
SELECt *
FROM Orders, LineItem
WHERE Order.order_id = LineItem.order_id
"""

mr = MapReduce.MapReduce()


def mapper(record):
    # key: order.id
    # value: the whole record
    key = record[1]
    value = record
    mr.emit_intermediate(key,value)


def reducer(key, list_of_values):
    # key: order.id
    # value: record

    # Each Order line is paired whith each LineItem line
    for i in list_of_values:
        if i[0] == "order":
            for j in list_of_values:
                if j[0] == "line_item":
                    mr.emit((i+j))
                    

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
