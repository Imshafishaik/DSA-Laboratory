import math

def cosine_similarity(user_a, user_b):
    dot = 0
    norm_a = 0
    norm_b = 0

    for i in range(len(user_a)):
        dot += user_a[i] * user_b[i]
        norm_a += user_a[i] ** 2
        norm_b += user_b[i] ** 2

    if norm_a == 0 or norm_b == 0:
        return 0

    return dot / (math.sqrt(norm_a) * math.sqrt(norm_b))

def top_k_similar_users(user_index, matrix, friends, k):
    similarities = []

    for i in range(len(matrix)):
        if i == user_index or i in friends:
            continue
        sim = cosine_similarity(matrix[user_index], matrix[i])
        similarities.append((i, sim))

    similarities.sort(key=lambda x: x[1], reverse=True)
    return similarities[:k]

def recommend_interests(user_index, matrix, similar_users):
    num_interests = len(matrix[0])
    recommendations = [0] * num_interests

    for user, _ in similar_users:
        for i in range(num_interests):
            if matrix[user_index][i] == 0:
                recommendations[i] += matrix[user][i]

    return recommendations

interest_matrix = [
    [10, 0, 8, 2, 5, 7],  
    [9, 1, 7, 3, 6, 8],   
    [2, 9, 1, 8, 3, 0]    
]

friends_of_user0 = set()  

print("Similarity for User 0 & User 1:", round(cosine_similarity(interest_matrix[0], interest_matrix[1]), 2))
print("Similarity for User 0 & User 2:", round(cosine_similarity(interest_matrix[0], interest_matrix[2]), 2))

top_users = top_k_similar_users(0, interest_matrix, friends_of_user0, k=2)
print("Top similar users:", top_users)

recommended = recommend_interests(0, interest_matrix, top_users)
print("Recommended interests:", recommended)
