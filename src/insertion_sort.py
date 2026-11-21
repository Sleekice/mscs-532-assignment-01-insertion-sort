
'''
    University of the Cumberlands
    Course: MSCS 532 - Algorithms and Data Structures
    Assignment 1: Insertion Sort

    Student: Peter Nwochie Tiewah
    Date: November 20, 2026
    File: src/insertion_sort.py

    Description:

    Insertion sort is a simple sorting algorithm that works by iteratively inserting each element of an unsorted list into its correct position in a sorted portion of the list.

    - Start with the second element as the first element is assumed to be sorted.
    - Compare the second element with the first if the second is smaller then swap them.
    - Move to the third element, compare it with the first two, and put it in its correct position
    - Repeat until the entire array is sorted.


    Time Complexity:
        Best Case: O(n)
            The array is already sorted in decreasing order.
            Each element requires only one key comparison,
            and no elements need to be shifted.

        Average Case: O(n^2)
            Elements require a varying number of comparisons
            and shifts to reach their correct positions.

        Worst Case: O(n^2)
            The array is sorted in increasing order.
            Each new element must be moved to the beginning
            of the sorted section.

    Auxiliary Space Complexity: O(1)
        The algorithm uses a fixed number of extra variables
        regardless of the number of elements in the array.

    Args:
        arr (list): A list of comparable numeric values.

    Returns:
        None: The original list is sorted in-place.
'''

def insertion_sort(arr):
    """
    Sorts a list of numbers in monotonically decreasing order
    using the Insertion Sort algorithm.

    Monotonically decreasing means each element is greater than
    or equal to the element that follows it.

    Example:
        Input:  [12, 11, 13, 5, 6]
        Output: [13, 12, 11, 6, 5]

    The algorithm works by dividing the array conceptually into
    two sections:
        1. A sorted section on the left.
        2. An unsorted section on the right.

    During each iteration, an element from the unsorted section
    is selected and inserted into its correct position within
    the sorted section.

    The original list is modified directly (in-place).
    """

    # Determine the total number of elements in the array.
    # This establishes how many elements we need to process.
    n = len(arr)

    # Begin at index 1 (the second element).
    # The first element, at index 0, is considered sorted
    # because a single element is already in sorted order.
    #
    # The loop processes each remaining element and inserts
    # it into the correct position within the sorted section.
    for i in range(1, n):

        # Store the current element in a temporary variable.
        # This is called the "key" because it is the value
        # we want to insert into the sorted section.
        #
        # Saving the key prevents its value from being lost
        # when other elements are shifted to the right.
        key = arr[i]

        # Set j to the index immediately before the key.
        #
        # We use j to move backward through the sorted section
        # and compare its elements with the key.
        j = i - 1

        # Continue moving backward while BOTH conditions hold:
        #
        # 1. j >= 0:
        #    We have not moved past the beginning of the array.
        #
        # 2. key > arr[j]:
        #    The key is larger than the element at index j.
        #
        # Because we want decreasing order, larger values
        # must appear before smaller values.
        #
        # Therefore, whenever the key is larger than arr[j],
        # we shift arr[j] one position to the right.
        #
        # The loop stops when:
        # - We reach the beginning of the array, OR
        # - We find an element greater than or equal to the key.
        while j >= 0 and key > arr[j]:

            # Copy the smaller element one position to the right.
            #
            # Example:
            # Before: [9, 6, 3, 7]
            #                  ^
            #                key = 7
            #
            # Since 7 > 3, shift 3 to the right:
            # After:  [9, 6, 3, 3]
            #
            # The value 7 remains safely stored in "key".
            arr[j + 1] = arr[j]

            # Move one position to the left.
            #
            # This allows the next iteration to compare the key
            # against the preceding element in the sorted section.
            #
            # Example:
            # j = 2 becomes j = 1.
            # We can now compare key = 7 against arr[1] = 6.
            j -= 1

        # The while loop has finished.
        #
        # At this point, j is either:
        # - The index of an element greater than or equal
        #   to the key, OR
        # - -1, meaning the key belongs at index 0.
        #
        # Insert the key immediately after index j.
        #
        # Example:
        # Before insertion: [9, 6, 6, 3]
        # Saved key: 7
        #
        # After insertion:  [9, 7, 6, 3]
        #
        # The sorted section now includes one additional element.
        arr[j + 1] = key


# This block runs only when this Python file is executed directly.
# It will not run automatically when the file is imported elsewhere,
# such as when running unit tests.
if __name__ == "__main__":

    # Create an example array containing unsorted numbers.
    # The expected decreasing order is [13, 12, 11, 6, 5].
    numbers = [12, 11, 13, 5, 6]

    # Display the original array before sorting.
    print("Before sorting:", numbers)

    # Call our insertion sort function.
    # The function modifies the original array directly.
    insertion_sort(numbers)

    # Display the array after the sorting operation.
    print("After sorting: ", numbers)
