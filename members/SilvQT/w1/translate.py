"""
Key differences compared to a C++ implementation:
- Requires allocating the exact size of the final container immediately, cannot dynamically append.
- Remaining elements cannot be cleanly extended using slices like `arr1[i:]`, instead, manual loops or `std::copy` must be used.
"""
def merge_sorted_arrays(arr1, arr2):
    i, j = 0, 0
    merged_array = []
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged_array.append(arr1[i])
            i+=1
        else:
            merged_array.append(arr2[j])
            j+=1
            
            
    while i < len(arr1):
        merged_array.append(arr1[i])
        i+=1
        
    while j < len(arr2):
        merged_array.append(arr2[j])
        j+=1
    
    
    return merged_array

