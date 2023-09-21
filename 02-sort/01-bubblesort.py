def bubblesort(arr: list):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


if __name__ == "__main__":
    data = [1, 0, 30, -2, 45, 0, 11, -9]
    bubblesort(data)
    print(data)
