from typing import List

def merge_sorted(arrays: List[List[int]]) -> List[int]:
    """
    Merge multiple sorted arrays into a single sorted array using concatenation and sorting.
    
    Args:
        arrays (List[List[int]]): A list of sorted arrays to be merged.
        
    Returns:
        List[int]: A single merged sorted array.
    """
    # Concatenate all arrays into a single list
    concatenated = []
    for arr in arrays:
        concatenated.extend(arr)
    
    # Sort the concatenated list
    concatenated.sort()
    
    return concatenated


# Example usage:
arrays1 = [
    [1, 3, 5, 7],
    [2, 4, 6, 8],
    [0, 9, 10, 11]
]
arrays2 = [
    [1, 3, 7],
    [2, 4, 8],
    [9, 10, 11]
]

print("Merged Array 1:", merge_sorted(arrays1))
# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

print("Merged Array 2:", merge_sorted(arrays2))
# Output: [1, 2, 3, 4, 7, 8, 9, 10, 11]
