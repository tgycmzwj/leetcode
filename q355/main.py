# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Twitter:
    def __init__(self):
        self.time=0
        self.following={} #follower:[followee]
        self.tweets={} #user: [(time,tweet)]
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets.keys():
            self.tweets[userId]=[]
        self.tweets[userId].append((self.time,tweetId))
        if userId not in self.following.keys():
            self.following[userId]=[]
        self.time=self.time+1
    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.following and userId not in self.tweets:
            return None
        followers=self.following[userId]+[userId]
        all_tweets=[]
        for follower in followers:
            all_tweets.append(self.tweets[follower])
        all_tweets=[item for sublist in all_tweets for item in sublist]
        all_tweets=sorted(all_tweets,key=lambda x:x[0],reverse=True)
        all_tweets=[x[1] for x in all_tweets]
        if len(all_tweets)>10:
            return all_tweets[:10]
        return all_tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following.keys():
            self.following[followerId]=[]
        if followeeId not in self.following[followerId]:
            self.following[followerId].append(followeeId)
        if followerId not in self.tweets.keys():
            self.tweets[followerId]=[]
        if followeeId not in self.tweets.keys():
            self.tweets[followeeId]=[]
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following.keys():
            if followeeId in self.following[followerId]:
                self.following[followerId].remove(followeeId)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cmds=["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
    vals=[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
    results=[]
    for i in range(len(cmds)):
        cmd,val=cmds[i],vals[i]
        if cmd=='Twitter':
            obj=Twitter()
            results.append(None)
        elif cmd=='postTweet':
            results.append(obj.postTweet(val[0],val[1]))
        elif cmd=='getNewsFeed':
            results.append(obj.getNewsFeed(val[0]))
        elif cmd=='follow':
            results.append(obj.follow(val[0],val[1]))
        elif cmd=='unfollow':
            results.append(obj.unfollow(val[0],val[1]))
    print(results)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
