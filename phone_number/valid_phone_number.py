nums = set(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])


def is_valid(phone_number):
    if phone_number[0] != "+":
        return False

    for i in range(1, len(phone_number)):
        if phone_number[i] not in nums:
            return False
    return True
