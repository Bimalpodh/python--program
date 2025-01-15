from collections import Counter

def intersect(arr1, arr2):
    # Count the occurrences of each element in both arrays
    count1 = Counter(arr1)
    count2 = Counter(arr2)
    
    # Find the intersection
    intersection = []
    for element in count1:
        if element in count2:
            # Append the minimum count of the element found in both arrays
            intersection.extend([element] * min(count1[element], count2[element]))
    
    return intersection

# Example usage
arr1 = [1,  2, 1,7,7,7,9]
arr2 = [2, 2,7,8,9,10,23,67]

result = intersect(arr1, arr2)
print(result)  # Output: [2, 2]
