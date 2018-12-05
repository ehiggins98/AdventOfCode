import re
import datetime
import numpy as np
import sys

days = {}

def parse_date_time(st):
    st = st[1:-1]
    st = re.split('[- :]', st)
    date = datetime.datetime(int(st[0]), int(st[1]), int(st[2]))
    hour, minute = int(st[3]), int(st[4])

    if int(st[3]) > 0:
        date = date + datetime.timedelta(days=1)
        hour, minute = -1, -1

    return date, hour, minute

with open('input.txt') as f:
    line = f.readline()
    while line != '':
        data = re.split(' ', line)
        event_type = data[2]
        date, hour, minute = parse_date_time(data[0] + ' ' + data[1])
        if event_type == 'Guard': event_type = 'begin'
        if event_type == 'falls': event_type = 'asleep'

        if date in days:
            days[date].append((event_type, data[3], hour, minute))
        else:
            days[date] = [(event_type, data[3], hour, minute)]
        line = f.readline()
guards = {}
for k, v in days.items():
    v.sort(key=lambda e: e[3])
    sleep = None
    awake = None
    id = v[0][1]

    for e in v[1:]:
        if e[0] == 'asleep':
            sleep, awake = e[3], None
        elif e[0] == 'wakes':
            awake = e[3]

        if sleep and awake:
            if id in guards:
                guards[id][sleep:awake] += 1
            else:
                guards[id] = np.zeros(60)
                guards[id][sleep:awake] += 1
            sleep = awake = None

max_id = 0
max_minute = 0
max_minute_count = 0
for k, v in guards.items():
    minute = np.argmax(v)
    minute_count = np.max(v)
    id = int(k[1:])

    if minute_count > max_minute_count:
        max_id = id
        max_minute = minute
        max_minute_count = minute_count
print(guards['#' + str(max_id)], max_id, max_minute)
print(max_id * max_minute)