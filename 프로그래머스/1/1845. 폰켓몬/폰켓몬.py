def solution(nums):
    pok = set(nums)
    if len(pok) >= len(nums)/2:
        return len(nums)/2
    elif len(pok) < len(nums)/2:
        return len(pok)
    