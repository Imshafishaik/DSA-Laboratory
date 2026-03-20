def friend_network(graph, user, visited=None):
    if visited is None:
        visited = set()

    visited.add(user)

    for friend in graph.get(user, []):
        if friend not in visited:
            friend_network(graph, friend, visited)

    return visited

def friend_suggestions(graph, user):
    direct_friends = set(graph.get(user, []))
    visited = friend_network(graph, user)

    suggestions = visited - direct_friends - {user}

    return suggestions

graph = {
    "Alice": ["Bob", "Charlie"],
    "Bob": ["Alice", "David"],
    "Charlie": ["Alice", "Emma"],
    "David": ["Bob"],
    "Emma": ["Charlie"]
}

print("Friend suggestions for Alice:", friend_suggestions(graph, "Alice"))