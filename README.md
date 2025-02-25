# Pretty Print Binary Tree

This project contains a Python script that builds a binary tree from a breadth-first (level-order) array representation and then pretty-prints it in a human-readable, top-down format. The output uses only the branch characters `/` and `\` (with no horizontal underscores) to visually connect parent nodes with their children.

## Overview

The binary tree is constructed from an array where:
- The first element is the root.
- Each subsequent element represents the next node in level-order (breadth-first) traversal.
- `None` indicates a missing node.

For example, the following array:
```python
[-9, -3, 2, None, 4, 4, 0, -6, None, -5]
```
represents a tree where:
- `-9` is the root.
- `-3` is the left child and `2` is the right child.
- `-3` has no left child (because of `None`) and its right child is `4`.
- `2` has `4` as its left child and `0` as its right child.
- And so on.

## Features

- **Tree Construction:** Builds a binary tree from a breadth-first list representation.
- **Pretty Printing:** Displays the tree in a top-down view with proper branch connections using `/` and `\`.
- **Customizable:** You can adjust the code to further refine spacing or output style if needed.

## File Structure

- `pretty_print_tree.py`  
  Contains the Python code that builds the tree and displays it in the desired format.

## How to Run

1. **Clone the Repository or Copy the Code:**

   Clone this repository or copy the provided `pretty_print_tree.py` file to your local machine.

2. **Run the Script:**

   Open your terminal, navigate to the directory containing the script, and run:
   ```bash
   python pretty_print_tree.py
   ```
   This will execute the code and print the binary tree based on the array defined in the script.

## Code Explanation

- **Tree Node Definition:**  
  A simple `Node` class holds the value and pointers to left and right children.

- **Tree Construction:**  
  The `build_tree` function converts a breadth-first list into a binary tree using a queue to maintain the order of insertion.

- **Tree Display:**  
  The `display` function, along with the helper `_display_aux`, recursively builds a list of strings that visually represents the tree.  
  - Only `/` and `\` are used to denote branch connections.
  - The tree is printed with the root at the top.

## Requirements

- Python 3.x
- No external libraries are required beyond Python's standard library.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Example Output

When you run the script with the example array, the output will look similar to:

```
 ___-9___  
 /        \ 
-3__      2 
    \    / \
    4    4 0
   /    /   
  -6   -5   
```

Feel free to modify the array or adjust the formatting in the code as needed for your application.

---

This README provides an overview of the project, explains the code structure, and gives instructions for running the script. You can further customize it according to your needs.