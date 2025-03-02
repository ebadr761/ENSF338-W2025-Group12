1.)

Some Advantages of array's is that for one, they are easy to use and the retrieval and replacement of elements is quick if the index is known O(1). This is because arrays store elements in a contiguous block of memory allowing direct access using indexing rather without needing traversal.

Some Disadvantages of array's is that adding/removing elements may be awkward because it requires
shifting elements left or right for insertion or deletion.
Another is that fixed size array's either limits the size of the list or wastes space, this is because resizing is expensive and predefined memory allocation could be a waste of memory
lastly, Dynamic sized array's require copying due to resizing when the allocated space capacity is exceeded.

Some Advantages of Linked Lists is that insertion at the head head  or tail (if the, tail pointer is used) is convenient O(1) because no shifting is required.
Linked lists also don't waste memory and allocates memory as needed. Dynamic memory allocation allows the list to grow or shrink as required by the program without the need for reallocating or resizing.

Some Disadvantages of array's is that Linked list have a slower access time complexity O(n). This is because the List has to be traversed through in order to access an element leading to a slower search speed.
They also have higher-memory usage due to the node requiring storage of next pointer. making it less efficient, especially is smaller datasets. Lastly, It requires careful memory handling to avoid to avoid issues such as null pointer dereferencing.

2.)

For fixed size replacement, to minimize the impact, simply overwrite the value at the target index this avoids shifting elements and keeps the operation O(1).
    ex) 
        def replace(list, index, new_value):
            list[index] = new_value  # Direct overwrite (O(1))

        arr = [1, 2, 3, 4, 5]
        replace(arr, 2, 10)
        print(arr)  # Output: [1, 2, 10, 4, 5]

For elements that are larger or smaller, slicing can help minimize shifts. This is required when a replacement for an individual element is multiple other elements or removal. If the element is the same size its o(1) but O(n) if list resizing is needed
    ex)
        def replace_with_shift(list, index, new_values):
            if isinstance(new_values, list):  # Multiple elements case
                list[index:index+1] = new_values
            else:
                list[index] = new_values  # Single element case

        arr = [1, 2, 3, 4, 5]
        replace_with_shift(arr, 2, [10, 11])  # Replacing 3 with two values
        print(arr)  # Output: [1, 2, 10, 11, 4, 5]

3.) 

When implementing a sorting function on a doubly linked list, 
Its required to consider how well the algorithm can handle linked list structures and whether
it requires random access(due to inefficiency in linked lists).

    1.) Insertion sort is feasible for small or nearly sorted lists but can be inefficient for large lists.
        It works well in linked lists because we can insert elements in-place
        without needing shifting operations. Since its a stable sort it maintains the order and can 
        run O(n) in best case performance but can also run O(n^2) in worst case performance.

    2.) Merge sort is very feasible and is a great choice for a doubly linked list due to its O(nlogn) complexity.
        Since merge sort doesn't rely on random access it more efficient for larger lists and always 
        runs O(nlogn), making it more feasible then insertion sort for larger lists. It's also a stable
        algorithm, so it maintains order. Since its a recursive algorithm however it does require a O(logn) 
        space complexity.

4.)
    Sorting algorithm | Best Case | Average Case | Worst Case
    
    Insertion Sort  |   O(n)     |   O(n^2)     |   O(n^2)
    Merge Sort      |   O(nlogn) |   O(nlogn)   |   O(nlogn)

    Insertion sort in a array requires finding the correct position by scanning elements
    from right to left O(n). Since in insertion process requires shifting all elements O(n)
    the total complexity is O(n^2) in worst and average case due to repeated shifting.

    Insertion sort in a doubly linked list requires traversing through the list to find the correct
    positioning O(n). Instead of shifting elements, pointers are updated O(1). The total complexity is
    still O(n^2) due to traversal through the list.

    Merge sort in a array splits the array requiring O(log n) recursive calls. Merging the two 
    halves requires O(n) extra space because new arrays are created. The total complexity is 
    O(nlogn) but requires additional space.

    Merge sort in a doubly linked list uses the fast and slow pointer technique O(n). This is where 
    the slow pointer moves one step at a time while the fast moves two steps at a time. When dealing
    with merging the two halves. pointer adjustment is used rather than copying elements O(1). 
    Making the total complexity O(nlogn) without extra space usage.








