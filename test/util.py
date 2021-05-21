import random
import string
import sys
from contextlib import contextmanager

from vert_tree.common import TreeNode

if sys.version_info[0] == 3:
    from io import StringIO
else:
    from io import BytesIO as StringIO


def create_tree_1():
    """
      a
     / \
    b   c
    """
    root = TreeNode("a")
    root.left = TreeNode("b")
    root.right = TreeNode("c")
    return root


def create_tree_2():
    """
          a
         / \
        /   \
       /     \
      b       c
     / \     / \
    d   e   f   g
    """
    root = create_tree_1()
    root.left.left = TreeNode("d")
    root.left.right = TreeNode("e")
    root.right.left = TreeNode("f")
    root.right.right = TreeNode("g")
    return root


def create_tree_3(add_left=True):
    """
                  a
                 / \
                /   \
               /     \
              /       \
             /         \
            /           \
           /             \
          b               c
         / \             / \
        /   \           /   \
       /     \         /     \
      d       e       f       g
     /                         \
    h            OR             h
    """
    root = create_tree_2()
    if add_left:
        root.left.left.left = TreeNode("h")
    else:
        root.right.right.right = TreeNode("h")
    return root


@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


def generate_random_name(min_chars=1, max_chars=20):
    node_val = ""
    for _ in range(random.randint(min_chars, max_chars)):
        node_val += random.choice(string.ascii_letters)
    return node_val


def generate_random_tree(depth, root=None):
    if depth == 0:
        return root
    if root is None:
        root = TreeNode(generate_random_name())
    node_children = random.choice(["left", "right", "both"])
    if node_children == "left":
        root.left = generate_random_tree(depth - 1, root.left)
    elif node_children == "right":
        root.right = generate_random_tree(depth - 1, root.right)
    else:
        root.left = generate_random_tree(depth - 1, root.left)
        root.right = generate_random_tree(depth - 1, root.right)
    return root
