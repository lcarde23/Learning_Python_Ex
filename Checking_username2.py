
current_users = ['Luis', 'John', 'Judy', 'Edgar', 'Rico']
new_users = ['Light', 'Judy', 'Gato', 'Admin', 'Dark']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print('This username is taken please use another.')
    else:
        print('This is a valid username.')
