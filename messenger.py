from datetime import datetime
from ast import literal_eval
import random as rd

server_data = {
    'users': [
        {'id': 41, 'name': 'Alice'},
        {'id': 23, 'name': 'Bob'}
    ],
    'channels': [
        {'id': 12, 'name': 'Town square', 'member_ids': [41, 23]}
    ],
    'messages': [
        {
            'id': 18,
            'reception_date': datetime.now(),
            'sender_id': 41,
            'channel': 12,
            'content': 'Hi 👋'
        }
    ]
}

def menu_input():
    choice = input('Do you want to go back to the principal menu (yes or no)? :')
    if choice == 'yes':
        menu()
    else:
        return('Bye!')

def users():

    utilisateurs = []
    identifiants = []

    print('---------option---------')
    print('print users : p')
    print('add user : a')
    print('back to the main menu : b')
    print('------------------------')

    for d in server_data['users']:
        utilisateurs.append(d['name'])
        identifiants.append(d['id'])

    choice = input('what do you want to do ? :')

    if choice == 'p' :
        print('------users list------')
        for k in range(len(utilisateurs)) :
            print('id :', identifiants[k], ', name :', utilisateurs[k])
        print('----------------------')
        users()

    elif choice == 'b':
        menu()

    elif choice == 'a':
        id = rd.randint(0, 1000)
        while id in identifiants :
            id = rd.randint(0, 1000)
        identifiants.append(id)
        choice2 = input('give a name :')
        server_data['users'].append({'id': id, 'name': choice2})
        users()


def channels():

    groups = []
    identifiants = []
    users = []

    for d in server_data['channels']:
        groups.append([ d['id'], d['name']])
        identifiants.append(d['id'])
    for d in server_data['users']:
        users.append([d['id'], d['name']])

    print('---------option---------')
    print('print groups : p')
    print('add group : a')
    print('back to the main menu : b')
    print('------------------------')

    choice = input('what do you want to do ? :')

    if choice == 'p':
        for k in range(len(groups)):
            print('id :', groups[k][0], ', name :', groups[k][1])
        channels()

    elif choice == 'b':
        menu()

    elif choice == 'a':
        id = rd.randint(0, 1000)
        while id in identifiants :
            id = rd.randint(0, 1000)
        identifiants.append(id)
        choice3 = input('give a name :')
        print('-----users id-----')
        for k in range(len(users)):
            print('id :', users[k][0], ', name :', users[k][1])
        print('------------------')
        choice4 = input('give a list of users to add (please give a list of ids) : ')
        server_data['channels'].append({'id': id, 'name': choice3, 'member_ids': literal_eval(choice4)})
        channels()


def messages():

    print('---------option---------')
    print('print messages of a group : p')
    print('back to the main menu : b')
    print('------------------------')

    choice = input('what do you want to do ? :')

    if choice == 'p':
        print('---group list---')
        identifiants = []
        for d in server_data['channels']:
            print('id :', d['id'], ', name :', d['name'])
            identifiants.append(d['id'])
        print('----------------')

        choice2 = input('give the id of the group : ')
        if not choice2.isdigit() or int(choice2) not in identifiants:
            print('Unknown group:', choice2)
            messages()
            return
        channel_id = int(choice2)

        # id -> nom pour retrouver l'envoyeur
        names = {}
        for d in server_data['users']:
            names[d['id']] = d['name']

        # messages du groupe, triés par date
        group_messages = []
        for d in server_data['messages']:
            if d['channel'] == channel_id:
                group_messages.append(d)
        group_messages.sort(key=lambda d: d['reception_date'])

        print('-----messages-----')
        if not group_messages:
            print('(no messages)')
        day = None
        for d in group_messages:
            date = d['reception_date']
            if date.date() != day
                day = date.date()
                print('------', day.strftime('%d/%m/%Y'), '------')
            sender = names.get(d['sender_id'], 'Unknown')
            print(date.strftime('%H:%M:%S'), '|', sender, ':', d['content'])
        print('------------------')
        messages()

    elif choice == 'b':
        menu()

    else:
        print('Unknown option:', choice)
        messages()


def menu():

    print('=== Messenger ===')
    print('u : users')
    print('m : messages')
    print('g : groups')
    print('x : exit')

    choice = input('Select an option between u, m, g, x :')

    if choice == 'x':
        print('Bye!')

    elif choice =='u':
        users()

    elif choice =='m':
        messages()
        
    elif choice =='g':
        channels()

    else:
        print('Unknown option:', choice)

menu()