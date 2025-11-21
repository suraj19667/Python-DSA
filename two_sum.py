def twoSum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        diff = target - num

        if diff in seen:
            return [seen[diff], i]

        seen[num] = i


# Example input
nums = [2, 7, 11, 15]
target = 9

# Function call
result = twoSum(nums, target)

print("Indexes:", result)
print("Numbers:", nums[result[0]], "+", nums[result[1]], "=", target)
