#  Divide-and-Conquer Sorting Algorithms: Quick Sort vs Merge Sort

This project demonstrates and compares the performance of two classic **divide-and-conquer** sorting algorithms — **Quick Sort** and **Merge Sort** — through Python implementation and benchmarking on various datasets.

---

## Project Structure

```
implementing-divide-and-conqure-algorithms/
├── sort_comparisons.py         # Runs and compares both algorithms
└── README.md                   # Project guide
```

---

## How to Run

1. **Create virtual environment (optional but recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install required libraries:**
   ```bash
   pip install memory-profiler
   ```

3. **Run the comparison script:**
   ```bash
   python3 sort_comparisons.py
   ```

You will see timing results printed for:
- Random data
- Already sorted data
- Reverse sorted data

---

##  What You'll Learn

- How **Quick Sort** and **Merge Sort** differ in speed and memory use
- How input order (random, sorted, reversed) impacts performance
- Why real-world results might differ from theoretical complexity

---

## Output Example

```
--- Random Data ---
Quick Sort Time: 0.0171 seconds
Merge Sort Time: 0.0306 seconds

--- Sorted Data ---
Quick Sort Time: 2.1606 seconds
Merge Sort Time: 0.0184 seconds

--- Reverse Sorted Data ---
Quick Sort Time: 1.4369 seconds
Merge Sort Time: 0.0168 seconds
```

---

## Author

Nouman Manwar  
Assignment 2: Analyzing and Implementing Divide-and Conquer Algorithms 
May 2025
