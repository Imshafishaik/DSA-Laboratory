class Post:
    def __init__(self, post_id, user_id, content, timestamp, likes, comments, shares):
        self.post_id = post_id
        self.user_id = user_id
        self.content = content
        self.timestamp = timestamp
        self.likes = likes
        self.comments = comments
        self.shares = shares
        self.engagement_score = likes + (2 * comments) + (3 * shares)

def max_engagement(posts, left, right):
    if left == right:
        return posts[left]

    mid = (left + right) // 2

    left_max = max_engagement(posts, left, mid)
    right_max = max_engagement(posts, mid + 1, right)

    return left_max if left_max.engagement_score > right_max.engagement_score else right_max

def total_engagement(posts, left, right):
    if left == right:
        return posts[left].engagement_score

    mid = (left + right) // 2

    return total_engagement(posts, left, mid) + total_engagement(posts, mid + 1, right)

def count_above_threshold(posts, left, right, threshold):
    if left == right:
        return 1 if posts[left].engagement_score > threshold else 0

    mid = (left + right) // 2

    return count_above_threshold(posts, left, mid, threshold) + \
           count_above_threshold(posts, mid + 1, right, threshold)

posts = [
    Post(1, "U1", "Post1", "10:00", 150, 0, 0),
    Post(2, "U2", "Post2", "10:10", 200, 50, 20),
    Post(3, "U3", "Post3", "10:20", 80, 5, 5)
]

max_post = max_engagement(posts, 0, len(posts)-1)

print("Highest engagement post:", max_post.post_id)
print("Total engagement:", total_engagement(posts, 0, len(posts)-1))