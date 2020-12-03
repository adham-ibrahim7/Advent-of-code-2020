file_loc = "../inputs/day1.txt"


def find2(nums):
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] + nums[j] == 2020:
                return nums[i] * nums[j]
    return -1


def find3(nums):
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            for k in range(j, len(nums)):
                if nums[i] + nums[j] + nums[k] == 2020:
                    return nums[i] * nums[j] * nums[k]
    return -1


if __name__ == "__main__":
    nums = []

    with open(file_loc, "r") as f:
        line = f.readline()
        while line != "":
            nums.append(int(line))
            line = f.readline()

    print(find3(nums))
