# O(log n)
Has this property when consecutive (1/2) operations are performed.

eg. Binary search is computed by consecutively cutting a sorted
array in half until the value in question is found.

Say the array has length of 16
1. arr.len() = 16
2. cut in half -> 16 * 1/2
3. cut in half -> 16 * (1/2)^2
4. ...
5. len = 1

This derives to :
* 16 * (1/2) ^ k = 1
* for n elements: n * (1/2) ^ k
* solving for number of operations: k = log_2 (n)

