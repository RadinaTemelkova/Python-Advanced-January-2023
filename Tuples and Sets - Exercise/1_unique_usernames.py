number_of_usernames = int(input())
usernames = set()

for x in range(number_of_usernames):
    current_username = input()
    usernames.add(current_username)

print("\n".join(usernames))
