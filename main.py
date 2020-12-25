import csv
from collections import defaultdict
from datetime import datetime


def main():
    exchanges = defaultdict(lambda: [])
    with open('trades.csv', 'r') as file:
        rows = csv.reader(file, delimiter=',')
        for row in rows:
            exchanges[row[3]].append(
                datetime.strptime(row[0], '%H:%M:%S.%f'))

    result = []
    for key in exchanges.keys():
        p_first, p_last = 0, 0
        max_length = 0
        cur_length = 0
        trades = exchanges.get(key)
        while p_last != len(trades):
            if (trades[p_last] - trades[p_first]).total_seconds() < 60:
                cur_length += 1
                p_last += 1
                continue
            max_length = max(max_length, cur_length)
            p_first += 1
            cur_length -= 1
        max_length = max(max_length, cur_length)
        result.append((key, max_length))

    for key, count in sorted(result):
        print(count)


if __name__ == "__main__":
    main()
