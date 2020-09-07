users = ['Ali', 'Jamal', 'Danish', 'Zeba', 'Waqar', 'Qirat']

# print(users[2])
print(users[0:3])
print(users[4:])

alot_zeros = [0]*20
print(alot_zeros)

# Unpacking
items = ['Laptop', 'Phone', 'Joystick']

# laptop = items[0]
# laptop, phone, joystick = items
laptop, *other = items

print(laptop)
print(other)


# Add Items
users.append('Python')
users.insert(0, 'Python')

users.pop()  # remove items

print(users)

