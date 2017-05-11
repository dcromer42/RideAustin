#/usr/bin/env python
# This script accepts two args, for start time and end time.

import pandas as pd
import sys
from dateutil import parser

ra=pd.read_csv(sys.argv[1], dtype=object, parse_dates=['completed_on','started_on','Date'])

start_datetime = parser.parse(sys.argv[2])
end_datetime = parser.parse(sys.argv[3])
print(start_datetime)
print(end_datetime)
print(type(start_datetime))
print(type(end_datetime))

selecta=ra[(ra['started_on']>start_datetime)&(ra['started_on']<=end_datetime)]

selecta.to_csv('Selecta.csv')
