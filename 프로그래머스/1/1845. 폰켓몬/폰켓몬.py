def solution(nums):
    answer = 0
    if len(nums)/2 >= len(set(nums)):
        return len(set(nums))
    elif len(nums)/2 < len(set(nums)):
        return len(nums)/2