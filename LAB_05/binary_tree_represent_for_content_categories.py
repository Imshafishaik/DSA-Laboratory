class CategoryNode:
    def __init__(self, category_id, name, post_count):
        self.category_id = category_id
        self.name = name
        self.post_count = post_count
        self.left = None
        self.right = None
        self.parent = None

def calculate_height(node):
    if node is None:
        return -1
    return 1 + max(calculate_height(node.left), calculate_height(node.right))


def calculate_node_height(node, target_id):
    if node is None:
        return -1

    if node.category_id == target_id:
        return 0

    left = calculate_node_height(node.left, target_id)
    right = calculate_node_height(node.right, target_id)

    if left != -1:
        return left + 1
    if right != -1:
        return right + 1

    return -1


def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


def count_leaves(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return count_leaves(node.left) + count_leaves(node.right)


def is_balanced(node):
    if node is None:
        return True

    left_h = calculate_height(node.left)
    right_h = calculate_height(node.right)

    if abs(left_h - right_h) > 1:
        return False

    return is_balanced(node.left) and is_balanced(node.right)


def is_full_binary_tree(node):
    if node is None:
        return True

    if node.left is None and node.right is None:
        return True

    if node.left and node.right:
        return is_full_binary_tree(node.left) and is_full_binary_tree(node.right)

    return False


def is_complete_binary_tree(root):
    queue = [root]
    found_null = False

    while queue:
        node = queue.pop(0)

        if node is None:
            found_null = True
        else:
            if found_null:
                return False
            queue.append(node.left)
            queue.append(node.right)

    return True


def find_category(node, category_id):
    if node is None:
        return None

    if node.category_id == category_id:
        return node

    left = find_category(node.left, category_id)
    if left:
        return left

    return find_category(node.right, category_id)


def find_path_to_root(node, category_id):
    if node is None:
        return []

    if node.category_id == category_id:
        return [node.name]

    left = find_path_to_root(node.left, category_id)
    if left:
        return left + [node.name]

    right = find_path_to_root(node.right, category_id)
    if right:
        return right + [node.name]

    return []


def lowest_common_ancestor(node, id1, id2):
    if node is None:
        return None

    if node.category_id == id1 or node.category_id == id2:
        return node

    left = lowest_common_ancestor(node.left, id1, id2)
    right = lowest_common_ancestor(node.right, id1, id2)

    if left and right:
        return node

    return left if left else right


if __name__ == "__main__":
    root = CategoryNode(1, "Technology", 150)

    root.left = CategoryNode(2, "Programming", 85)
    root.right = CategoryNode(3, "Design", 65)

    root.left.left = CategoryNode(4, "Python", 42)
    root.left.right = CategoryNode(5, "Java", 30)

    root.left.left.left = CategoryNode(6, "Django", 18)
    root.left.left.right = CategoryNode(7, "Flask", 12)

    root.right.left = CategoryNode(8, "UI/UX", 38)
    root.right.right = CategoryNode(9, "Graphics", 22)

    print("Tree Height:", calculate_height(root))
    print("Node Height (Java):", calculate_node_height(root, 5))
    print("Total Nodes:", count_nodes(root))
    print("Leaf Nodes:", count_leaves(root))
    print("Is Balanced:", is_balanced(root))

    print("Find Category (Python):", find_category(root, 4).name)

    print("Path to Root (Django):", find_path_to_root(root, 6))

    lca = lowest_common_ancestor(root, 6, 5)
    print("LCA (Django & Java):", lca.name if lca else None)