def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.
    """
    if not list_of_integers:
        return None

    low = 0
    high = len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2
        mid_value = list_of_integers[mid]
        next_value = list_of_integers[mid + 1]

        if mid_value < next_value:
            # The peak must be on the right side of mid
            low = mid + 1
        else:
            # The peak must be on the left side of mid or mid itself
            high = mid

    return list_of_integers[low]

# Test cases
if __name__ == "__main__":
    print(find_peak([1, 2, 4, 6, 3]))          # Output: 6
    print(find_peak([4, 2, 1, 2, 3, 1]))      # Output: 3
    print(find_peak([2, 2, 2]))               # Output: 2
    print(find_peak([]))                     # Output: None
    print(find_peak([-2, -4, 2, 1]))         # Output: 2
    print(find_peak([4, 2, 1, 2, 2, 2, 3, 1])) # Output: 4
