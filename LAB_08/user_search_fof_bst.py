class BSTNode:
    def __init__(self, user_id, name, friends=None):
        self.user_id = user_id
        self.name    = name
        self.friends = friends or []
        self.left    = None
        self.right   = None


class UserBST:
    def __init__(self):
        self.root = None


    def insert(self, user_id, name, friends=None):
        self.root = self._insert(self.root, user_id, name, friends or [])

    def _insert(self, node, user_id, name, friends):
        if node is None:
            return BSTNode(user_id, name, friends)
        if user_id < node.user_id:
            node.left  = self._insert(node.left,  user_id, name, friends)
        elif user_id > node.user_id:
            node.right = self._insert(node.right, user_id, name, friends)
        return node

    def find(self, user_id):
        return self._find(self.root, user_id)

    def _find(self, node, user_id):
        if node is None:
            return None
        if user_id == node.user_id:
            return node
        if user_id < node.user_id:
            return self._find(node.left,  user_id)
        return self._find(node.right, user_id)

    def inorder_traversal(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node is None:
            return
        self._inorder(node.left, result)
        result.append(node.user_id)
        self._inorder(node.right, result)

    def delete(self, user_id):
        self.root = self._delete(self.root, user_id)

    def _delete(self, node, user_id):
        if node is None:
            return None
        if user_id < node.user_id:
            node.left  = self._delete(node.left,  user_id)
        elif user_id > node.user_id:
            node.right = self._delete(node.right, user_id)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            successor       = self._find_min(node.right)
            node.user_id    = successor.user_id
            node.name       = successor.name
            node.friends    = successor.friends
            node.right      = self._delete(node.right, successor.user_id)
        return node

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node


    def suggest_friends(self, user_id, max_suggestions=5):
        user = self.find(user_id)
        if user is None:
            return []

        direct = set(user.friends)
        fof_count = {}

        for fid in user.friends:
            friend_node = self.find(fid)
            if friend_node is None:
                continue
            for fof_id in friend_node.friends:
                if fof_id != user_id and fof_id not in direct:
                    fof_count[fof_id] = fof_count.get(fof_id, 0) + 1

        ranked = sorted(fof_count.items(),
                        key=lambda x: x[1], reverse=True)
        return [(uid, count) for uid, count in ranked[:max_suggestions]]


    def get_height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))

    def is_balanced(self):
        return self._balanced(self.root)

    def _balanced(self, node):
        if node is None:
            return True
        lh = self._height(node.left)
        rh = self._height(node.right)
        if abs(lh - rh) > 1:
            return False
        return self._balanced(node.left) and self._balanced(node.right)

    def get_leaf_count(self):
        return self._leaves(self.root)

    def _leaves(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self._leaves(node.left) + self._leaves(node.right)
    
def test_exercise1():
    bst = UserBST()

    bst.insert(5,  "Alice",   [2, 8, 3])
    bst.insert(3,  "Bob",     [5, 1, 7])
    bst.insert(8,  "Charlie", [5, 9])
    bst.insert(1,  "Dave",    [3])
    bst.insert(7,  "Eve",     [3, 9])
    bst.insert(9,  "Frank",   [8, 7])
    bst.insert(2,  "Grace",   [5])

    assert bst.find(5).name == "Alice"
    assert bst.find(99) is None

    order = bst.inorder_traversal()
    assert order == sorted(order)

    bst.delete(1)
    assert bst.find(1) is None
    assert bst.inorder_traversal() == sorted([5,3,8,7,9,2])

    bst.delete(3)
    assert bst.find(3) is None
    assert bst.inorder_traversal() == sorted([5,8,7,9,2])

   
    bst2 = UserBST()
    bst2.insert(1, "A", [2, 3])
    bst2.insert(2, "B", [1, 4, 5])
    bst2.insert(3, "C", [1, 5, 6])
    bst2.insert(4, "D", [2])
    bst2.insert(5, "E", [2, 3])
    bst2.insert(6, "F", [3])
    sugg = bst2.suggest_friends(1, max_suggestions=5)
    ids = [s[0] for s in sugg]
    assert 4 in ids
    assert 5 in ids   
    assert 6 in ids  
    assert 1 not in ids
    assert 2 not in ids   
    assert sugg[0][0] == 5 

    balanced_bst = UserBST()
    for uid in [4, 2, 6, 1, 3, 5, 7]:
        balanced_bst.insert(uid, f"user{uid}", [])
    assert balanced_bst.get_height() == 3
    assert balanced_bst.is_balanced() == True

    degenerate = UserBST()
    for uid in [1, 2, 3, 4, 5]:
        degenerate.insert(uid, f"u{uid}", [])
    assert degenerate.get_height() == 5
    assert degenerate.is_balanced() == False

    assert balanced_bst.get_leaf_count() == 4

    bst.delete(999)  
    assert bst.suggest_friends(999) == []

    print("Exercise 1: ALL TESTS PASSED")

test_exercise1()