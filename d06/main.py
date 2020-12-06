# Advent of Code Day 6
# Custom customs
# in Python
# d-toth1

def count_chars(s, c):
    counts = {i: s.count(i) for i in set(s)}
    vals = [1 for v in counts.values() if v == c]

    return sum(vals)

def parse_entries(file):
    with open(file) as f:
        data = f.read().splitlines()

    groups1 = []
    groups2 = []
    group_string = ""
    count = 0

    for i in data:
        if i != "":
            group_string += i
            count += 1

        else:
            groups1.append(len(set(group_string)))

            if count == 1:
                groups2.append(len(set(group_string)))

            else:
                groups2.append(count_chars(group_string, count))

            group_string = ""
            count = 0

    # Get the last group
    groups1.append(len(set(group_string)))

    if count == 1:
        groups2.append(len(set(group_string)))

    else:
        groups2.append(count_chars(group_string, count))


    return sum(groups1), sum(groups2)

def main():
    file = "input.txt"
    print(parse_entries(file))

if __name__ == "__main__":
    main()
