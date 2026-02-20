def intersection(set1, set2):
    return set1 & set2

def difference(set1, set2):
    return set1 - set2

def union(set1, set2):
    return set1 | set2

def jaccard_similarity(set1, set2):
    inter = intersection(set1, set2)
    uni = union(set1, set2)
    if len(uni) == 0:
        return 0
    return len(inter) / len(uni)

def suggest_friends(user, friend_map):
    user_friends = friend_map[user]
    suggestions = set()

    for friend in user_friends:
        for fof in friend_map.get(friend, set()):
            if fof != user and fof not in user_friends:
                suggestions.add(fof)

    return suggestions


userA = {101, 102, 103, 104, 105}
userB = {103, 104, 106, 107, 108}

print("Mutual friends:", intersection(userA, userB))
print("Unique to A:", difference(userA, userB))
print("Unique to B:", difference(userB, userA))
print("Union:", union(userA, userB))
print("Jaccard similarity:", jaccard_similarity(userA, userB))

friend_map = {
    1: {2, 3},
    2: {1, 4, 5},
    3: {1, 6},
    4: {2},
    5: {2},
    6: {3}
}

print("Suggested friends for user 1:", suggest_friends(1, friend_map))
