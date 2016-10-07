import vk
from getpass import getpass


APP_ID = 5658578


def get_user_login():
    return input('Enter your login (email or telephone number) : ')
    

def get_user_password():
    return getpass('Enter your password: ')


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    list_of_id_online_friends = api.friends.getOnline()
    list_of_online_friends = api.users.get(user_ids=list_of_id_online_friends)
    return list_of_online_friends


def output_friends_to_console(friends_online):
    print('Online users are ')
    for user in friends_online:
        print('id={} Name:{} {}'.format(user['uid'], user['first_name'], \
            user['last_name']))


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
