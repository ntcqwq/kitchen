from collections import defaultdict

N, Q = map(int, input().split())
a = list(map(int, input().split()))

# Preprocess the array to count occurrences of each element
element_counts = defaultdict(int)
for num in a:
    element_counts[num] += 1

# Process queries
for _ in range(Q):
    l, r = map(int, input().split())
    unique_elements = set(a[l-1:r])

    has_zero = 0 in unique_elements
    has_positive = any(num > 0 for num in unique_elements)
    has_negative = any(num < 0 for num in unique_elements)

    if has_zero or (has_positive and has_negative):
        print("YES")
    else:
        # Check if there is any element with more than one occurrence
        for num in unique_elements:
            if element_counts[num] > 1:
                print("YES")
                break
        else:
            print("NO")
