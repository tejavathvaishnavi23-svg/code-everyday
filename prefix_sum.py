arr = [2, 1, 6, 4]

count = 0

for i in range(len(arr)):

    even_sum = 0
    odd_sum = 0
    new_index = 0

    for j in range(len(arr)):

        if j == i:
            continue

        if new_index % 2 == 0:
            even_sum += arr[j]
        else:
            odd_sum += arr[j]

        new_index += 1

    if even_sum == odd_sum:
        count += 1

print(count)
