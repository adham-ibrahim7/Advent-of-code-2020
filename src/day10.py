f = open("../inputs/day10.txt", "r")

nums = [int(s) for s in f.read().split("\n")]
nums.sort()

nums = [0] + nums + [nums[-1] + 3]

diff1 = sum(nums[i+1] - nums[i] == 1 for i in range(len(nums)-1))
diff3 = sum(nums[i+1] - nums[i] == 3 for i in range(len(nums)-1))

print("p1:", diff1 * diff3)

dp = [1]
for i in range(1, len(nums)):
    dp.append(0)

    j = i-1
    while j >= 0 and nums[i] - nums[j] <= 3:
        dp[i] += dp[j]
        j -= 1

print("p2:", dp[-1])
