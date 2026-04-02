class CategoryNode:
    def __init__(self, category_id, name, post_count):
        self.category_id = category_id
        self.name = name
        self.post_count = post_count
        self.left = None
        self.right = None
        self.parent = None

class GenNode:
    def __init__(self, category_id, name, post_count):
        self.category_id = category_id
        self.name = name
        self.post_count = post_count
        self.children = []
        self.parent = None


def binary_to_generalized(node):
    if node is None:
        return None

    gen = GenNode(node.category_id, node.name, node.post_count)

    if node.left:
        gen.children.append(binary_to_generalized(node.left))
    if node.right:
        gen.children.append(binary_to_generalized(node.right))

    return gen


def generalized_to_binary(node):
    if node is None:
        return None

    root = CategoryNode(node.category_id, node.name, node.post_count)

    if node.children:
        root.left = generalized_to_binary(node.children[0])

        current = root.left
        for child in node.children[1:]:
            current.right = generalized_to_binary(child)
            current = current.right

    return root

def pre_order_generalized(node):
    if node is None:
        return

    print(node.name)

    for child in node.children:
        pre_order_generalized(child)


def post_order_generalized(node):
    if node is None:
        return

    for child in node.children:
        post_order_generalized(child)

    print(node.name)


def level_order_generalized(node):
    if node is None:
        return

    queue = [node]

    while queue:
        current = queue.pop(0)
        print(current.name)

        for child in current.children:
            queue.append(child)

def calculate_height_generalized(node):
    if node is None:
        return -1

    if not node.children:
        return 0

    return 1 + max(calculate_height_generalized(child) for child in node.children)
def pre_order_export(node, level=0):
    if node is None:
        return

    print(" " * (level * 4) + f"{node.name}({node.post_count})")

    pre_order_export(node.left, level + 1)
    pre_order_export(node.right, level + 1)


def count_nodes_generalized(node):
    if node is None:
        return 0

    return 1 + sum(count_nodes_generalized(child) for child in node.children)


def count_leaves_generalized(node):
    if node is None:
        return 0

    if not node.children:
        return 1

    return sum(count_leaves_generalized(child) for child in node.children)


def calculate_fan_out(node):
    if node is None:
        return 0

    max_children = len(node.children)

    for child in node.children:
        max_children = max(max_children, calculate_fan_out(child))

    return max_children


def calculate_branching_factor(node):
    if node is None:
        return (0, 0)

    if not node.children:
        return (0, 0)

    total_children = len(node.children)
    total_nodes = 1

    for child in node.children:
        c, n = calculate_branching_factor(child)
        total_children += c
        total_nodes += n

    return (total_children, total_nodes)

if __name__ == "__main__":

    root = GenNode(1, "Technology", 150)

    prog = GenNode(2, "Programming", 85)
    design = GenNode(3, "Design", 65)
    business = GenNode(10, "Business", 50)

    root.children = [prog, design, business]

    python = GenNode(4, "Python", 42)
    java = GenNode(5, "Java", 30)
    prog.children = [python, java]

    django = GenNode(6, "Django", 18)
    flask = GenNode(7, "Flask", 12)
    python.children = [django, flask]

    design.children = [
        GenNode(8, "UI/UX", 38),
        GenNode(9, "Graphics", 22)
    ]

    business.children = [
        GenNode(11, "Finance", 20),
        GenNode(12, "Marketing", 15),
        GenNode(13, "HR", 10)
    ]

    print("Pre-order Generalized:")
    pre_order_generalized(root)

    print("\nPost-order Generalized:")
    post_order_generalized(root)

    print("\nLevel-order Generalized:")
    level_order_generalized(root)

    print("\nHeight:", calculate_height_generalized(root))
    print("Total Nodes:", count_nodes_generalized(root))
    print("Leaf Nodes:", count_leaves_generalized(root))
    print("Fan-out:", calculate_fan_out(root))

    total_children, total_nodes = calculate_branching_factor(root)
    if total_nodes > 0:
        print("Branching Factor:", total_children / total_nodes)

    binary_root = generalized_to_binary(root)
    print("\nConverted to Binary Tree (Pre-order):")
    pre_order_export(binary_root)