class CategoryNode:
    def __init__(self, category_id, name, post_count):
        self.category_id = category_id
        self.name = name
        self.post_count = post_count
        self.left = None
        self.right = None
        self.parent = None


def in_order_collect(node):
    if node is None:
        return []
    return (
        in_order_collect(node.left)
        + [node.name]
        + in_order_collect(node.right)
    )


def in_order_find_kth(node, k, counter=[0]):
    if node is None:
        return None

    left = in_order_find_kth(node.left, k, counter)
    if left:
        return left

    counter[0] += 1
    if counter[0] == k:
        return node

    return in_order_find_kth(node.right, k, counter)


def pre_order_export(node, level=0):
    if node is None:
        return

    print(" " * (level * 4) + f"{node.name}({node.post_count})")

    pre_order_export(node.left, level + 1)
    pre_order_export(node.right, level + 1)


def pre_order_copy(node):
    if node is None:
        return None

    new_node = CategoryNode(node.category_id, node.name, node.post_count)
    new_node.left = pre_order_copy(node.left)
    new_node.right = pre_order_copy(node.right)

    return new_node


def pre_order_serialize(node):
    if node is None:
        return ""

    result = f"{node.name}({node.post_count})|"
    return result + pre_order_serialize(node.left) + pre_order_serialize(node.right)


def post_order_total_posts(node):
    if node is None:
        return 0

    return (
        post_order_total_posts(node.left)
        + post_order_total_posts(node.right)
        + node.post_count
    )


def post_order_collect_leaves(node):
    if node is None:
        return []

    if node.left is None and node.right is None:
        return [node.name]

    return post_order_collect_leaves(node.left) + post_order_collect_leaves(node.right)


def find_most_popular_category(node):
    if node is None:
        return None

    max_node = node

    left = find_most_popular_category(node.left)
    right = find_most_popular_category(node.right)

    if left and left.post_count > max_node.post_count:
        max_node = left

    if right and right.post_count > max_node.post_count:
        max_node = right

    return max_node


def category_with_most_subcategories(node):
    if node is None:
        return None

    max_node = node
    max_children = int(node.left is not None) + int(node.right is not None)

    left = category_with_most_subcategories(node.left)
    right = category_with_most_subcategories(node.right)

    for child in [left, right]:
        if child:
            count = int(child.left is not None) + int(child.right is not None)
            if count > max_children:
                max_children = count
                max_node = child

    return max_node

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

    print("In-order:")
    print(in_order_collect(root))

    print("\nPre-order Export:")
    pre_order_export(root)

    print("\nSerialized Tree:")
    print(pre_order_serialize(root))

    print("\nTotal Posts (Post-order):")
    print(post_order_total_posts(root))

    print("\nLeaf Categories:")
    print(post_order_collect_leaves(root))

    print("\nMost Popular Category:")
    print(find_most_popular_category(root).name)

    print("\nCategory with Most Subcategories:")
    print(category_with_most_subcategories(root).name)