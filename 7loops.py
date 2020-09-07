
users = ['Ali', 'Jamal', 'Danish', 'Zeba', 'Waqar', 'Qirat']

# name = list('Edwin')
# print(name)

my_list = list(range(0, 10))
print(my_list)

# For loop
for user in users:
    print(user)

for i in range(0, 20):
    print('I run 20 times')

name = 'Edwin'

for letter in name:
    print(letter)

# While Loop
age = 10
while age < 20:
    print('I am running')
    age += 1
    if age == 14:
        print('I am independent now')
        # break
        continue
