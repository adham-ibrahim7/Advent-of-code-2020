f = open("../inputs/day14.txt", "r")

instructions = f.read().split("\n")

memory = {}
mask = ""

for instruction in instructions:
    if instruction[0:4] == "mask":
        mask = instruction[7:]
    else:
        split = instruction.split("] = ")
        address = int(split[0][4:])
        value = int(split[1])

        value_str = bin(value)[2:]
        value_str = "0" * (len(mask) - len(value_str)) + value_str

        after_mask = ""
        for i in range(len(mask)):
            after_mask += mask[i] if mask[i] != "X" else value_str[i]

        value_after_mask = int(after_mask, 2)
        memory[address] = value_after_mask

print("p1:", sum(memory.values()))

memory.clear()
for instruction in instructions:
    if instruction[0:4] == "mask":
        mask = instruction[7:]
    else:
        split = instruction.split("] = ")
        address = int(split[0][4:])
        value = int(split[1])

        address_str = bin(address)[2:]
        address_str = "0" * (len(mask) - len(address_str)) + address_str

        after_mask = ""
        for i in range(len(mask)):
            after_mask += mask[i] if mask[i] != "0" else address_str[i]

        def recurse(i, curr):
            if i == len(after_mask):
                memory[int(curr, 2)] = value
                return
            if after_mask[i] != "X":
                recurse(i+1, curr + after_mask[i])
            else:
                recurse(i+1, curr + "0")
                recurse(i+1, curr + "1")

        recurse(0, "")

print("p2:", sum(memory.values()))