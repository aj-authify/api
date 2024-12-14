nums = set(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])


def is_valid(tpo):
    for char in tpo:
        if char not in nums:
            return False

    return True
