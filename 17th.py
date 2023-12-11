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
__________________________________________________________________________________________________________________________________
python
# Take input from the user
n = int(input("How many students' percentages do you want to store? "))
percentages = []

# Loop to get the percentages
for i in range(n):
    percentage = float(input(f"Enter the percentage for student {i+1}: "))
    percentages.append(percentage)

# Bucket sort function
def bucket_sort(arr):
    n = len(arr)
    buckets = [[] for _ in range(n)]

    for num in arr:
        index = int(num * n)
        buckets[index].append(num)

    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))

    return sorted_arr

# Sort the array using bucket sort
sorted_percentages = bucket_sort(percentages)

# Display the top five scores
top_five_scores = sorted_percentages[-5:]
print("The top five scores are:", top_five_scores)
