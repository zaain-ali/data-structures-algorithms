def find_two_numbers(nums: list[int], target: int):
    seen = {}

    for index, num in enumerate(nums):
        needed = target - num

        if num in seen:
            return [seen[num], index]
        
        seen[needed] = index

print(find_two_numbers([3, 2, 4], 6))  # [1, 2]
print(find_two_numbers([3, 3], 6))     # [0, 1]
