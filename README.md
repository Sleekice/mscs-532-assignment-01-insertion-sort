# MSCS 532 — Assignment 1: Insertion Sort

**Student:** Peter Nwochie Tiewah
**Institution:** University of the Cumberlands
**Course:** MSCS 532 — Algorithms and Data Structures
**Assignment:** Assignment 1 — Insertion Sort
**Date:** November 20, 2026
**Programming Language:** Python 3

---

## 1. Project Overview

This project implements the **Insertion Sort algorithm** in Python, as introduced in Chapter 2 of *Introduction to Algorithms* by Cormen et al.

The assignment requires modifying the traditional insertion sort algorithm to arrange elements in **monotonically decreasing order**, rather than the commonly demonstrated increasing order.

The program sorts the input list in place, meaning it modifies the original list without creating a separate list to store the sorted elements.

The repository also includes automated tests to verify that the algorithm correctly handles different input scenarios.

## 2. Understanding Insertion Sort

Insertion sort is a comparison-based sorting algorithm that builds a sorted portion of an array one element at a time.

The algorithm conceptually divides the array into two sections:

1. **Sorted section:** Contains elements already arranged in the required order.
2. **Unsorted section:** Contains elements that have not yet been processed.

Initially, the first element is considered sorted because a single element does not require comparisons to establish its order.

Starting from the second element, the algorithm selects a value called the **key**, compares it against elements in the sorted section, and shifts elements when necessary to make room for the key.

This process continues until the entire array is sorted.

### Monotonically Decreasing Order

A sequence is monotonically decreasing when each element is greater than or equal to the next element.

Mathematically:

$$
a_1 \geq a_2 \geq a_3 \geq \cdots \geq a_n
$$

For example:

**Original array:**

```text
[12, 11, 13, 5, 6]
```

**Expected output:**

```text
[13, 12, 11, 6, 5]
```

Unlike increasing-order insertion sort, the descending implementation shifts smaller elements to the right when the selected key is larger.

## 3. Algorithm Implementation

The implementation is located in `src/insertion_sort.py`.

```python
def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # Shift smaller elements one position to the right
        # to make room for the current key.
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert the key into its correct position.
        arr[j + 1] = key
```

### Explanation of the Implementation

- `n = len(arr)` determines the number of elements in the input list.
- `range(1, n)` begins processing at the second element because the first element is initially considered sorted.
- `key = arr[i]` temporarily stores the current element being inserted.
- `j = i - 1` identifies the element immediately preceding the key.
- `j >= 0` ensures the algorithm does not move beyond the beginning of the array.
- `key > arr[j]` checks whether the key is larger than the preceding element. If it is, that smaller element must move right.
- `arr[j + 1] = arr[j]` shifts the smaller element one position to the right.
- `j -= 1` moves the comparison one position backward.
- `arr[j + 1] = key` inserts the saved key into its correct position.

The key difference from traditional ascending insertion sort is the comparison condition:

**Ascending order:**

```python
while j >= 0 and key < arr[j]:
```

**Descending order:**

```python
while j >= 0 and key > arr[j]:
```

Changing this comparison allows the algorithm to arrange larger values before smaller values.

## 4. Step-by-Step Execution

Consider the input array:

```text
[12, 11, 13, 5, 6]
```

| Iteration | Selected Key | Array After Insertion |
| --------- | ------------ | --------------------- |
| Initial   | —            | `[12, 11, 13, 5, 6]`  |
| 1         | 11           | `[12, 11, 13, 5, 6]`  |
| 2         | 13           | `[13, 12, 11, 5, 6]`  |
| 3         | 5            | `[13, 12, 11, 5, 6]`  |
| 4         | 6            | `[13, 12, 11, 6, 5]`  |

### Iteration Analysis

**Iteration 1:** The key is `11`. It is compared against `12`. Since `11 > 12` is false, no shifting occurs.

**Iteration 2:** The key is `13`. Since `13` is greater than both `11` and `12`, those elements shift right, and `13` is inserted at the beginning.

**Iteration 3:** The key is `5`. Since `5` is smaller than `11`, it remains in its current position.

**Iteration 4:** The key is `6`. Since `6 > 5`, the value `5` shifts right. The algorithm then compares `6` with `11`. Because `6 > 11` is false, the key is inserted before `5`.

The final result is:

```text
[13, 12, 11, 6, 5]
```

## 5. Time Complexity Analysis

Insertion sort's running time depends on the initial arrangement of elements.

Let `n` represent the number of elements in the input array.

### Best Case — O(n)

The best case occurs when the array is already sorted in monotonically decreasing order.

Example:

```text
[9, 7, 5, 3, 1]
```

During each outer-loop iteration, the selected key is compared against the preceding element.

Because the array is already correctly ordered, the inner loop does not shift any elements.

The number of key comparisons is:

$$
T(n)=n-1
$$

Therefore, the running time grows linearly with the number of elements:

$$
T(n)=\Theta(n)
$$

### Worst Case — O(n²)

The worst case occurs when the input array is sorted in increasing order.

Example:

```text
[1, 2, 3, 4, 5]
```

Since the algorithm must sort in decreasing order, each new key must be inserted at the beginning of the sorted section.

The number of key comparisons across successive iterations is:

$$
T(n)=1+2+3+\cdots+(n-1)
$$

Using the arithmetic series formula:

$$
T(n)=\frac{n(n-1)}{2}
$$

Expanding:

$$
T(n)=\frac{n^2-n}{2}
$$

The dominant term is $n^2$. Ignoring constant factors and lower-order terms gives:

$$
T(n)=\Theta(n^2)
$$

### Average Case — O(n²)

For a uniformly random ordering of distinct elements, each key is expected to move past approximately half of the elements preceding it.

The expected number of shifts is:

$$
E[S(n)]=\frac{1}{2}\sum_{i=1}^{n-1}i
$$

Therefore:

$$
E[S(n)]=\frac{n(n-1)}{4}
$$

Since the dominant term is quadratic, the expected running time is:

$$
E[T(n)]=\Theta(n^2)
$$

### Complexity Summary

| Case    | Time Complexity | Explanation                        |
| ------- | --------------- | ---------------------------------- |
| Best    | O(n)            | Already sorted in decreasing order |
| Average | O(n²)           | Randomly ordered elements          |
| Worst   | O(n²)           | Sorted in increasing order         |

## 6. Space Complexity Analysis

Insertion sort performs its operations directly on the original array.

The implementation uses a fixed number of additional variables:

- `n` stores the length of the array.
- `i` represents the current position.
- `key` temporarily stores the selected element.
- `j` tracks comparisons within the sorted section.

The number of extra variables does not increase with the input size.

Therefore, the auxiliary space complexity is:

$$
S(n)=O(1)
$$

This makes insertion sort an **in-place sorting algorithm**.

## 7. Project Structure

```text
mscs-532-assignment-01-insertion-sort/
│
├── src/
│   └── insertion_sort.py
│
├── tests/
│   └── test_insertion_sort.py
│
├── .gitignore
└── README.md
```

**File descriptions:**

- `src/insertion_sort.py` — Main insertion sort implementation and example execution.
- `tests/test_insertion_sort.py` — Automated tests for validating sorting behavior.
- `.gitignore` — Excludes local environment files and generated Python files from version control.
- `README.md` — Project documentation, implementation explanation, and complexity analysis.

## 8. Running the Program

### Requirements

- Python 3
- PyCharm or another Python-compatible development environment

### Execute the Program

From the project root directory, run:

```bash
python src/insertion_sort.py
```

On systems where Python 3 is invoked through `python3`, use:

```bash
python3 src/insertion_sort.py
```

### Expected Output

```text
Before sorting: [12, 11, 13, 5, 6]
After sorting:  [13, 12, 11, 6, 5]
```

## 9. Testing

The project includes automated tests for several scenarios:

| Test Scenario            | Purpose                                               |
| ------------------------ | ----------------------------------------------------- |
| Unsorted array           | Verify correct descending sorting                     |
| Already decreasing array | Verify that an already sorted input remains unchanged |
| Increasing array         | Verify correct worst-case behavior                    |
| Duplicate values         | Verify that equal values are handled correctly        |
| Empty array              | Verify safe handling of an empty input                |

### Running Tests

Install pytest if needed:

```bash
python -m pip install pytest
```

Run the tests from the project root:

```bash
python -m pytest
```

All tests should pass when the implementation is correct.

## 10. Conclusion

This assignment demonstrates how insertion sort works and how a small change in its comparison condition can reverse the sorting order.

The implementation sorts elements into monotonically decreasing order by repeatedly inserting each selected key into its correct position within the sorted portion of the array.

The analysis also demonstrates that insertion sort has linear best-case running time, quadratic average- and worst-case running time, and constant auxiliary space usage.

Although insertion sort becomes less efficient for large input arrays, its straightforward implementation, in-place operation, and efficiency for small or nearly sorted inputs make it a valuable algorithm for understanding sorting techniques and algorithm analysis.

## Reference

Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). *Introduction to algorithms* (4th ed.). MIT Press.
