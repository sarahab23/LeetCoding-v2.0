class Twitter:

    def __init__(self):
        self.time = 0
        self.userFollowee = defaultdict(set) # user id -> set of followeeId
        self.userPosts = defaultdict(list) # user id -> list of [time, post id]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userPosts[userId].append([-self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        allPosts = [post for f in self.userFollowee[userId] for post in self.userPosts[f]] 
        allPosts.extend(self.userPosts[userId])
        heapq.heapify(allPosts) # allPosts - min heap
        if len(allPosts) > 10:
            for i in range(10): res.append(heapq.heappop(allPosts)[1])
        else: 
            for i in range(len(allPosts)): res.append(heapq.heappop(allPosts)[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userFollowee[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.userFollowee[followerId]:
            self.userFollowee[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)