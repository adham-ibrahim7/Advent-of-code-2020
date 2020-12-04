import re


def is_valid(info):
    fields = 0
    for pair in info:
        key, val = pair.split(":")
        if key == "cid":
            continue
        fields += 1

        if key == "byr":
            b = int(val)
            if b < 1920 or b > 2002:
                return False
        elif key == "iyr":
            i = int(val)
            if i < 2010 or i > 2020:
                return False
        elif key == "eyr":
            i = int(val)
            if i < 2020 or i > 2030:
                return False
        elif key == "hgt":
            if val[-2:] == "cm":
                if not val[:-2].isnumeric():
                    return False
                cm = int(val[:-2])
                if cm < 150 or cm > 193:
                    return False
            else:
                if not val[:-2].isnumeric():
                    return False
                inch = int(val[:-2])
                if inch < 59 or inch > 76:
                    return False
        elif key == "hcl":
            if val[0] != "#":
                return False
            for c in val[1:]:
                if c not in "0123456789abcdef":
                    return False
        elif key == "ecl":
            if val not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                return False
        else:
            if len(val) != 9:
                return False
            for c in val:
                if c not in "0123456789":
                    return False

    return fields == 7


if __name__ == "__main__":
    with open("../inputs/day4.txt", "r") as f:
        passports = f.read().split("\n\n")

        print(len(passports))

        ans = 0

        for passport in passports:
            info = re.split("[ \n]", passport)
            ans += is_valid(info)

        print(ans)
