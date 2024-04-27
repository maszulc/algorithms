import time
from arrays import Arrays


input_data = [
    [1, 2, 3, 1],
    [1, 2, 3, 4],
    [1, 1, 1, 3, 3, 4, 3, 2, 4, 2],
]

start_time = time.time()
for nums in input_data:
    print(Arrays.contains_duplicate1(nums))
end_time = time.time()
execution_time = end_time - start_time
print(f"Duplicate check list count() method time: {execution_time}")

start_time = time.time()
for nums in input_data:
    print(Arrays.contains_duplicate2(nums))
end_time = time.time()
execution_time = end_time - start_time
print(f"Duplicate check with hashset time: {execution_time}")
