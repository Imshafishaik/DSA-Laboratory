class SocialGraph:
    def __init__(self, num_users: int):
        self.n = num_users
        self.num_edges = 0
        self.matrix = [[False] * num_users for _ in range(num_users)]
        self.adj_list = {u: set() for u in range(num_users)}


    def add_friendship(self, u: int, v: int):
        if u == v or self.matrix[u][v]:
            return  
        self.matrix[u][v] = True
        self.matrix[v][u] = True
        self.adj_list[u].add(v)
        self.adj_list[v].add(u)
        self.num_edges += 1

    def remove_friendship(self, u: int, v: int):
        if not self.matrix[u][v]:
            return
        self.matrix[u][v] = False
        self.matrix[v][u] = False
        self.adj_list[u].discard(v)
        self.adj_list[v].discard(u)
        self.num_edges -= 1

    def are_friends(self, u: int, v: int) -> bool:
        return self.matrix[u][v]               

    def get_friends(self, u: int) -> set:
        return self.adj_list[u]

    def get_degree(self, u: int) -> int:
        return len(self.adj_list[u])

    def get_num_users(self) -> int:
        return self.n

    def get_num_edges(self) -> int:
        return self.num_edges


    def is_complete_graph(self) -> bool:
        max_possible = self.n * (self.n - 1) // 2
        return self.num_edges == max_possible

    def graph_density(self) -> float:
        if self.n <= 1:
            return 0.0
        return (2 * self.num_edges) / (self.n * (self.n - 1))

    def degree_distribution(self) -> dict:
        dist = {}
        for u in range(self.n):
            d = self.get_degree(u)
            dist[d] = dist.get(d, 0) + 1
        return dist

    def matrix_to_list(self) -> dict:
        result = {u: set() for u in range(self.n)}
        for u in range(self.n):
            for v in range(self.n):
                if self.matrix[u][v]:
                    result[u].add(v)
        return result

    def list_to_matrix(self) -> list:
        result = [[False] * self.n for _ in range(self.n)]
        for u, neighbors in self.adj_list.items():
            for v in neighbors:
                result[u][v] = True
        return result
    
def test_exercise1():
    g = SocialGraph(5)
    g.add_friendship(0, 1)
    g.add_friendship(0, 2)
    g.add_friendship(1, 2)
    g.add_friendship(3, 4)

    assert g.are_friends(0, 1) == True
    assert g.are_friends(0, 3) == False
    assert g.get_degree(0) == 2
    assert g.get_num_edges() == 4

    g.remove_friendship(0, 1)
    assert g.are_friends(0, 1) == False
    assert g.get_num_edges() == 3

    g.add_friendship(0, 2)  
    assert g.get_num_edges() == 3

    g.add_friendship(0, 0)   
    assert g.are_friends(0, 0) == False

    g2 = SocialGraph(3)
    g2.add_friendship(0, 1)
    g2.add_friendship(1, 2)
    g2.add_friendship(0, 2)
    assert g2.is_complete_graph() == True
    assert abs(g2.graph_density() - 1.0) < 0.001
    assert g2.degree_distribution()[2] == 3

    assert g2.matrix_to_list()[0] == {1, 2}
    assert g2.list_to_matrix()[0][1] == True

    g3 = SocialGraph(1)
    assert g3.is_complete_graph() == True
    assert g3.graph_density() == 0.0

    print("ALL TESTCASES PASSED")

test_exercise1()