f = open("../inputs/day9.txt", "r")

nums = [int(s) for s in f.read().split("\n")]
subset_size = 25

subset = set(nums[0:subset_size])


def two_sum(num):
    for n in subset:
        if num - n in subset and num - n != n:
            return True
    return False


ans1 = 0

for i in range(subset_size, len(nums)):
    if not two_sum(nums[i]):
        ans1 = nums[i]
        break
    subset.remove(nums[i-subset_size])
    subset.add(nums[i])

print("p1:", ans1)

for i in range(0, len(nums)):
    for j in range(i+1, len(nums)):
        if sum(nums[i:j+1]) == ans1:
            print("p2:", min(nums[i:j+1]) + max(nums[i:j+1]))
