class Post:
    def __init__(self, post_id, user_id, content, likes, comments, shares):
        self.post_id = post_id
        self.user_id = user_id
        self.content = content
        self.likes = likes
        self.comments = comments
        self.shares = shares
        self.engagement_score = likes + 2*comments + 3*shares
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.head = None
        self.count = 0

    def enqueue(self, post):
        if self.head is None or post.engagement_score > self.head.engagement_score:
            post.next = self.head
            self.head = post
        else:
            current = self.head
            while current.next and current.next.engagement_score >= post.engagement_score:
                current = current.next
            post.next = current.next
            current.next = post
        self.count += 1

    def dequeue_max(self):
        if self.head is None:
            return None
        temp = self.head
        self.head = self.head.next
        self.count -= 1
        return temp

    def peek_max(self):
        return self.head

    def size(self):
        return self.count

    def get_top_k(self, k):
        result = []
        temp = self.head
        while temp and k > 0:
            result.append(temp.content)
            temp = temp.next
            k -= 1
        return result

pq = PriorityQueue()

pq.enqueue(Post(1,101,"Post1",20,10,5))
pq.enqueue(Post(2,102,"Post2",10,5,2))
pq.enqueue(Post(3,103,"Post3",30,20,10))

print("Top Post:", pq.peek_max().content)
print("Top 2 Posts:", pq.get_top_k(2))