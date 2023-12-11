def bucket_sort(arr):
    buckets = [[] for _ in range(len(arr))]

    for x in arr:
        bucket_index = int(len(arr) * x)
        buckets[bucket_index].append(x)

    for bucket in buckets:
        bucket.sort()

    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)
    return sorted_arr

percentage = [23.7,89.7,67.5,45.6,33.6,66.8,90.8]

sorted_percentage = bucket_sort(percentage)

print("top five scores:")
for i in range(5):
    print(sorted_percentage[i])
