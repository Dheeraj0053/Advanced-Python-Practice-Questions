def listOperations(lst):
    print("a. Fourth item:", lst[3] if len(lst) >= 4 else "None")
    print("b. All except first two:", lst[2:])
    print("c. Reversed list:", lst[::-1])
    print("d. Sum of elements:", sum(lst))
    print("e. Max and min:", max(lst), min(lst))
    print("f. First zero index:", next((i for i, x in enumerate(lst) if x == 0), -1))
    print("g. Sorted (ascending):", sorted(lst))
    print("   Sorted (descending):", sorted(lst, reverse=True))

listOperations([1, 2, 3, 4, 5, 0, -1])