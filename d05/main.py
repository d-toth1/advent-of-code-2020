# Advent of Code Day 5
# Binary Boarding
# in Python
# d-toth1

def decode_line(l):
    """
    Decodes a single line
    """
    row = l[:7]
    col = l[7:]
    row_num = list(range(128))
    col_num = list(range(8))

    for r in row:
        n = len(row_num) // 2

        if r == "F":
            row_num = row_num[:n]

        else:
            row_num = row_num[n:]

    for c in col:
        n = len(col_num) // 2

        if c == "L":
            col_num = col_num[:n]

        else:
            col_num = col_num[n:]

    return row_num[0]*8 + col_num[0]

def main():
    file = "input.txt"

    with open(file) as f:
        data = f.read().splitlines()

    ids = [decode_line(i) for i in data]
    ids = sorted(ids)
    print(max(ids))

    ii = ids[0]

    for i in ids:
        if ii != i:
            print(ii)
            break

        ii += 1

if __name__ == "__main__":
    main()
