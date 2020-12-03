def breakdown_policy(policy_str):
    policy_str = policy_str.split("-")
    a = int(policy_str[0])
    policy_str = policy_str[1].split(" ")
    b = int(policy_str[0])
    char = policy_str[1]

    return a, b, char


def isValid1(password, policy):
    least, greatest, char = breakdown_policy(policy)

    count = 0
    for c in password:
        if char == c:
            count += 1

    return least <= count <= greatest


def isValid2(password, policy):
    a, b, char = breakdown_policy(policy)

    return (password[a - 1] == char) ^ (password[b - 1] == char)


if __name__ == "__main__":
    with open("../inputs/day2.txt", "r") as f:
        count = 0
        line = f.readline()
        while line != "":
            policy, password = line.split(": ")
            if isValid2(password, policy):
                count += 1
            line = f.readline()
        print(count)
