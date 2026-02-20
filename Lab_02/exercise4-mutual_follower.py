class FollowerMatrix:
    def __init__(self, size, user_count):
        self.size = size
        self.user_count = user_count
        self.matrix = [[False] * size for _ in range(size)]

    def follow(self, follower, followee):
        self.matrix[follower][followee] = True

    def unfollow(self, follower, followee):
        self.matrix[follower][followee] = False

    def is_following(self, follower, followee):
        return self.matrix[follower][followee]

    def get_followers(self, user):
        followers = []
        for i in range(self.user_count):
            if self.matrix[i][user]:
                followers.append(i)
        return followers

    def get_following(self, user):
        following = []
        for j in range(self.user_count):
            if self.matrix[user][j]:
                following.append(j)
        return following

    def get_mutual_follows(self):
        mutual = []
        for i in range(self.user_count):
            for j in range(i + 1, self.user_count):
                if self.matrix[i][j] and self.matrix[j][i]:
                    mutual.append((i, j))
        return mutual

    def influence_score(self, user):
        followers = len(self.get_followers(user))
        following = len(self.get_following(user))
        return (followers + following) / self.user_count


fm = FollowerMatrix(size=3, user_count=3)

fm.follow(0, 1)  
fm.follow(1, 0)  
fm.follow(1, 2)  

print("User 0 followers:", fm.get_followers(0))
print("User 0 following:", fm.get_following(0))
print("Mutual follows:", fm.get_mutual_follows())

print("Influence User 0:", fm.influence_score(0))
print("Influence User 1:", fm.influence_score(1))
print("Influence User 2:", fm.influence_score(2))