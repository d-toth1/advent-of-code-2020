# Advent of Code Day 4
# Passport Processing
# in Python
# d-toth1

def parse_line(l):
    """ Parse a single line """
    fields = {}
    l = l.split(" ")

    for i in l:
        col = i.index(":")
        fields[i[:col]] = i[col+1:]

    return fields

def parse_entries(file):
    """ Parse lines of file
    to form a list of dicts.

    """
    lst = []

    with open(file) as f:
        lines = f.read().splitlines()

        passport = {}

        for l in lines:

            if l != "":
                passport.update(parse_line(l))

            else:
                lst.append(passport)
                passport = {}

        lst.append(passport) # Get the last one

    return lst

def check_valid(p):
    return all(i in p for i in ("byr", "iyr", "eyr", "hgt",
                                "hcl", "ecl", "pid"))

def complex_check(p):
    """ Checks if all seven conditions
    are met.

    """
    checks = 0
    simple_check = check_valid(p)

    if simple_check:
        for k,v in p.items():
            if k == "byr":
                if 1920 <= int(v) <= 2002:
                    checks += 1

            elif k == "iyr":
                if 2010 <= int(v) <= 2020:
                    checks += 1

            elif k == "eyr":
                if 2020 <= int(v) <= 2030:
                    checks += 1

            elif k == "hgt":
                if "cm" in v:
                    c = v.index("c")
                    if 150 <= int(v[:c]) <= 193:
                        checks += 1
                elif "in" in v:
                    i = v.index("i")
                    if 59 <= int(v[:i]) <= 76:
                        checks += 1
                else:
                    pass

            elif k == "hcl":
                if (v[0] == "#") and (len(v[1:])==6) and (v[1:].isalnum()):
                    checks += 1

            elif k == "ecl":
                if v in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
                    checks += 1

            elif k == "pid":
                if (len(v) == 9) and (v.isnumeric()):
                    checks += 1

            else:
                continue

    return checks == 7



def main():
    file = "input.txt"
    data = parse_entries(file)
    valid1 = sum([check_valid(i) for i in data])
    valid2 = sum([complex_check(i) for i in data])
    print("No. of simple valid passports: ", valid1)
    print("No. of complex valid passports: ", valid2)


if __name__ == "__main__":
    main()
