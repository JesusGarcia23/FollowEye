import instaloader
import getpass
from colorama import Fore, init


loader = instaloader.Instaloader()

init(autoreset=True)

print(Fore.BLUE + "-- Welcome to FollowEye -- (Check who is not following you back on Instagram)")

username = input("Username: ")
password = getpass.getpass(prompt='Password: ')

# log into user account
loader.login(username, password)

# get user profile
profile = instaloader.Profile.from_username(loader.context, username)

# followers list
followerList = []
count = 0

# following list
followingList = []
secondCount = 0

# people who is not following back list
noFollowBackList = []
thirdCount = 0;

print("Getting list of people you follow...")

# get following
for followee in profile.get_followees():
    followingList.append(followee.username)
    file = open(username + "_following.txt","a+")
    file.write(followingList[count])
    file.write("\n")
    file.close()
    count = count + 1

print("Done!")

print("Getting list of people following you...")
# get followers
for follower in profile.get_followers():
    followerList.append(follower.username)
    file = open(username + "_followers.txt","a+")
    file.write(followerList[secondCount])
    file.write("\n")
    file.close()
    secondCount = secondCount + 1

print("Done!")


print("Checking who is not following you back")

# Check who is not following back
for followee in followingList:
    if followee not in followerList:
        noFollowBackList.append(followee)
        file = open(username + "_noFollowBack.txt","a+")
        file.write(followerList[thirdCount])
        file.write("\n")
        file.close()
        thirdCount = thirdCount + 1

# print list of people who does not follow back
for notFollower in noFollowBackList:
    print(Fore.RED + notFollower)
