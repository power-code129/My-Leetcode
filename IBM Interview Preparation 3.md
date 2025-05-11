# Diagonally Sort a Matrix

## Problem Statement

A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or the leftmost column and going in the bottom-right direction until reaching the matrix's end.

For example, the matrix diagonal starting from `mat[2][0]`, where `mat` is a 6 x 3 matrix, includes cells `mat[2][0]`, `mat[3][1]`, and `mat[4][2]`.

Given an `m x n` matrix `mat` of integers, sort each matrix diagonal in **ascending order** and return the resulting matrix.

---

## Input Format

- The first line contains two space-separated integers `M` and `N`, representing the number of rows and columns in the matrix.
- The next `M` lines each contain `N` space-separated integers, representing the elements of the matrix `mat`. Each line corresponds to a row in the matrix.

---

## Output Format

- Print the diagonally sorted matrix.
- Each row of the matrix should be printed on a new line, as space-separated integers.

---

## Constraints

- `1 <= M, N <= 10^2`
- `1 <= mat[i][j] <= 10^2`

---

## Sample Testcase 0

**Input**
```

3 4
3 3 1 1
2 2 1 2
1 1 2 2

```

**Output**
```

2 1 1 1
1 2 2 2
1 2 3 3

```

---

## Sample Testcase 1

**Input**
```

3 3
3 1 1
2 5 2
4 2 2

```

**Output**
```

2 1 1
2 3 2
4 2 5

````

---

## Explanation

- Diagonal starting at `mat[0][0]`: `[3, 5, 2]` → Sorted: `[2, 3, 5]`
- Diagonal starting at `mat[0][1]`: `[1, 2]` → Sorted: `[1, 2]`
- Diagonal starting at `mat[1][0]`: `[2, 2]` → Sorted: `[2, 2]`

---

## Python Code

```python
def diagonal_sort(mat):
    """
    Sort each diagonal of the matrix in ascending order.
    Parameters:
        mat (list of list of int): The matrix to be sorted
    Returns:
        list of list of int: The diagonally sorted matrix
    """
    from collections import defaultdict

    m = len(mat)
    n = len(mat[0])
    diagonals = defaultdict(list)

    # Step 1: Group elements by the diagonal key (i - j)
    for i in range(m):
        for j in range(n):
            diagonals[i - j].append(mat[i][j])

    # Step 2: Sort each diagonal in reverse order to use pop()
    for key in diagonals:
        diagonals[key].sort(reverse=True)

    # Step 3: Write sorted values back into the matrix
    for i in range(m):
        for j in range(n):
            mat[i][j] = diagonals[i - j].pop()

    return mat


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    m = int(data[0])
    n = int(data[1])
    
    mat = []
    index = 2
    for i in range(m):
        row = list(map(int, data[index:index + n]))
        mat.append(row)
        index += n
    
    # Call user logic function
    sorted_mat = diagonal_sort(mat)
    
    # Print the sorted matrix
    for row in sorted_mat:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()
````

