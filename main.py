def build_unique_array(full_name: str) -> list[str]:
    unique_letters = []
    for char in full_name.upper():
        if char.isalpha() and char not in unique_letters:
            unique_letters.append(char)
    return unique_letters


def bubble_sort(arr: list[str]) -> list[str]:
    sorted_arr = arr.copy()
    n = len(sorted_arr)

    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                swapped = True
        if not swapped:
            break

    return sorted_arr


if __name__ == "__main__":
    full_name = "JEANELLE UNABIA"

    unsorted_array = build_unique_array(full_name)
    sorted_array = bubble_sort(unsorted_array)

    print("=== ASSESSMENT 3.7: SORTING ALGORITHMS ===\n")
    print("Full Name     :", full_name)
    print("Unsorted Array:", unsorted_array)
    print("Sorted Array  :", sorted_array)