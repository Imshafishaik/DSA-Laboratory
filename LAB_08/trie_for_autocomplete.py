class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_username = False
        self.user_id = None


class AutocompleteTrie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, username, user_id):
        node = self.root
        for c in username.lower():
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end_of_username = True
        node.user_id = user_id

    def search(self, username):
        node = self.root
        for c in username.lower():
            if c not in node.children:
                return None
            node = node.children[c]
        return node.user_id if node.is_end_of_username else None

    def starts_with(self, prefix):
        node = self.root
        for c in prefix.lower():
            if c not in node.children:
                return False
            node = node.children[c]
        return True

    def autocomplete(self, prefix, max_results=10):
        node = self.root
        for c in prefix.lower():
            if c not in node.children:
                return []

            node = node.children[c]

        results = []
        self._collect(node, prefix.lower(), results, max_results)
        return results

    def _collect(self, node, word, results, max_results):
        if len(results) >= max_results:
            return

        if node.is_end_of_username:
            results.append((word, node.user_id))

        # NOTE: Removed repeated sorting for efficiency
        for char in node.children:
            self._collect(node.children[char], word + char, results, max_results)

    def delete(self, username):
        self._delete(self.root, username.lower(), 0)

    def _delete(self, node, username, depth):
        if node is None:
            return None

        if depth == len(username):
            if node.is_end_of_username:
                node.is_end_of_username = False
                node.user_id = None
            return node if node.children else None

        c = username[depth]
        if c in node.children:
            child = self._delete(node.children[c], username, depth + 1)

            if child is None:
                del node.children[c]
            else:
                node.children[c] = child

        if not node.is_end_of_username and not node.children:
            return None

        return node

    def count_words(self):
        return self._count(self.root)

    def _count(self, node):
        if node is None:
            return 0

        count = 1 if node.is_end_of_username else 0
        for child in node.children.values():
            count += self._count(child)
        return count

    def get_total_nodes(self):
        return self._total_nodes(self.root)

    def _total_nodes(self, node):
        if node is None:
            return 0

        count = 1
        for child in node.children.values():
            count += self._total_nodes(child)
        return count

    def get_height(self):
        return self._height(self.root)

    def _height(self, node):
        if not node.children:
            return 0
        return 1 + max(self._height(c) for c in node.children.values())


# ────────────────────────────────────────────────────────────────

class ActivitySegmentTree:
    def __init__(self, activity_array):
        self.n = len(activity_array)
        self.data = list(activity_array)

        if self.n == 0:
            self.tree = []
            self.max_tree = []
            self.min_tree = []
            return

        self.tree = [0] * (4 * self.n)
        self.max_tree = [0] * (4 * self.n)
        self.min_tree = [0] * (4 * self.n)

        self._build(1, 0, self.n - 1)

    def _build(self, node, start, end):
        if start == end:
            self.tree[node] = self.data[start]
            self.max_tree[node] = self.data[start]
            self.min_tree[node] = self.data[start]
            return

        mid = (start + end) // 2

        self._build(2 * node, start, mid)
        self._build(2 * node + 1, mid + 1, end)

        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]
        self.max_tree[node] = max(self.max_tree[2 * node], self.max_tree[2 * node + 1])
        self.min_tree[node] = min(self.min_tree[2 * node], self.min_tree[2 * node + 1])

    def _validate(self, l, r):
        if self.n == 0:
            raise ValueError("Segment tree is empty")
        if l < 0 or r >= self.n or l > r:
            raise ValueError(f"Invalid range [{l}, {r}]")

    def query(self, l, r):
        self._validate(l, r)
        return self._query(1, 0, self.n - 1, l, r)

    def _query(self, node, start, end, l, r):
        if r < start or end < l:
            return 0

        if l <= start and end <= r:
            return self.tree[node]

        mid = (start + end) // 2

        return (
            self._query(2 * node, start, mid, l, r) +
            self._query(2 * node + 1, mid + 1, end, l, r)
        )

    def get_range_max(self, l, r):
        self._validate(l, r)
        return self._range_max(1, 0, self.n - 1, l, r)

    def _range_max(self, node, start, end, l, r):
        if r < start or end < l:
            return float('-inf')

        if l <= start and end <= r:
            return self.max_tree[node]

        mid = (start + end) // 2

        return max(
            self._range_max(2 * node, start, mid, l, r),
            self._range_max(2 * node + 1, mid + 1, end, l, r)
        )

    def get_range_min(self, l, r):
        self._validate(l, r)
        return self._range_min(1, 0, self.n - 1, l, r)

    def _range_min(self, node, start, end, l, r):
        if r < start or end < l:
            return float('inf')

        if l <= start and end <= r:
            return self.min_tree[node]

        mid = (start + end) // 2

        return min(
            self._range_min(2 * node, start, mid, l, r),
            self._range_min(2 * node + 1, mid + 1, end, l, r)
        )

    def get_tree_size(self):
        return len(self.tree)

    def get_height(self):
        import math
        if self.n <= 1:
            return 1
        return math.ceil(math.log2(self.n)) + 1

    def get_leaf_values(self):
        return list(self.data)


# ────────────────────────────────────────────────────────────────

def test_exercise3():
    # Trie tests
    trie = AutocompleteTrie()
    trie.insert("alice", 1)
    trie.insert("alice123", 2)
    trie.insert("bob", 3)
    trie.insert("bobby", 4)
    trie.insert("charlie", 5)
    trie.insert("chad", 6)

    assert trie.search("alice") == 1
    assert trie.search("bob") == 3
    assert trie.search("xyz") is None
    assert trie.search("alice12") is None

    assert trie.starts_with("ali") is True
    assert trie.starts_with("xyz") is False

    assert trie.autocomplete("xyz") == []

    ac = trie.autocomplete("ali")
    names = [r[0] for r in ac]
    assert "alice" in names
    assert "alice123" in names
    assert "bob" not in names

    ac_bob = trie.autocomplete("bo")
    assert len(ac_bob) == 2

    ac_limit = trie.autocomplete("", max_results=2)
    assert len(ac_limit) == 2

    assert trie.count_words() == 6

    trie.delete("bob")
    assert trie.search("bob") is None
    assert trie.search("bobby") == 4

    trie.delete("xyz")
    assert trie.count_words() == 5

    # Segment Tree tests
    data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    st = ActivitySegmentTree(data)

    assert st.query(0, 9) == sum(data)
    assert st.query(0, 0) == 3
    assert st.query(2, 5) == 19
    assert st.query(7, 9) == 14

    assert st.get_range_max(0, 9) == 9
    assert st.get_range_max(0, 4) == 5
    assert st.get_range_min(0, 9) == 1
    assert st.get_range_min(5, 9) == 2

    assert st.query(4, 4) == 5
    assert st.get_range_max(4, 4) == 5
    assert st.get_range_min(4, 4) == 5

    try:
        st.query(-1, 5)
        assert False
    except ValueError:
        pass

    try:
        st.query(0, 100)
        assert False
    except ValueError:
        pass

    print("Exercise 3: ALL TESTS PASSED")


if __name__ == "__main__":
    test_exercise3()