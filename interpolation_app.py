import tkinter as tk
from tkinter import ttk
import time


def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1
    comparisons = 0

    while low <= high and arr[low] <= target <= arr[high]:
        comparisons += 1

        if low == high:
            if arr[low] == target:
                return low, comparisons
            return -1, comparisons

        pos = low + int(
            ((target - arr[low]) * (high - low))
            / (arr[high] - arr[low])
        )

        if arr[pos] == target:
            return pos, comparisons
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1, comparisons


def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    comparisons = 0

    while low <= high:
        comparisons += 1

        mid = (low + high) // 2

        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons


def start_search():
    try:
        arr = list(map(int, array_entry.get().split(',')))
        arr.sort()

        target = int(target_entry.get())

        start = time.perf_counter()
        idx_i, comp_i = interpolation_search(arr, target)
        time_i = (time.perf_counter() - start) * 1000

        start = time.perf_counter()
        idx_b, comp_b = binary_search(arr, target)
        time_b = (time.perf_counter() - start) * 1000

        result_text.delete("1.0", tk.END)

        result_text.insert(
            tk.END,
            f"Sorted Array:\n{arr}\n\n"
        )

        if idx_i != -1:
            result_text.insert(
                tk.END,
                f"✅ Found at Index: {idx_i}\n\n"
            )
        else:
            result_text.insert(
                tk.END,
                "❌ Element Not Found\n\n"
            )

        result_text.insert(
            tk.END,
            "📊 PERFORMANCE ANALYSIS\n"
            "--------------------------------\n"
            f"Interpolation Search\n"
            f"Comparisons : {comp_i}\n"
            f"Time        : {time_i:.6f} ms\n\n"
            f"Binary Search\n"
            f"Comparisons : {comp_b}\n"
            f"Time        : {time_b:.6f} ms\n"
        )

    except:
        result_text.delete("1.0", tk.END)
        result_text.insert(
            tk.END,
            "Please enter valid numbers."
        )


root = tk.Tk()
root.title("AI Search Visualizer")
root.geometry("900x600")
root.configure(bg="#121212")

title = tk.Label(
    root,
    text="🔍 SEARCH ALGORITHM VISUALIZER",
    font=("Arial", 24, "bold"),
    fg="cyan",
    bg="#121212"
)
title.pack(pady=20)

frame = tk.Frame(root, bg="#121212")
frame.pack()

tk.Label(
    frame,
    text="Enter Array",
    font=("Arial", 12),
    fg="white",
    bg="#121212"
).grid(row=0, column=0, pady=10)

array_entry = tk.Entry(
    frame,
    width=50,
    font=("Arial", 12)
)
array_entry.grid(row=0, column=1)

array_entry.insert(
    0,
    "23,45,53,60,78,94"
)

tk.Label(
    frame,
    text="Target",
    font=("Arial", 12),
    fg="white",
    bg="#121212"
).grid(row=1, column=0, pady=10)

target_entry = tk.Entry(
    frame,
    width=20,
    font=("Arial", 12)
)
target_entry.grid(row=1, column=1)

search_btn = tk.Button(
    root,
    text="⚡ START SEARCH",
    font=("Arial", 14, "bold"),
    bg="cyan",
    command=start_search
)
search_btn.pack(pady=20)

result_text = tk.Text(
    root,
    height=18,
    width=80,
    font=("Consolas", 11),
    bg="#1e1e1e",
    fg="white"
)
result_text.pack()

root.mainloop()