from datetime import datetime
from ast import literal_eval

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

m = []
for d in server_data['messages']:
    m.append(d['content'])

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
        for n in utilisateurs :
            print(n)
        print('----------------------')
        users()
    elif choice == 'b':
        menu()
    elif choice == 'a':
        choice2 = input('give an id :')
        while int(choice2) in identifiants :
            choice2 = input('this id is already taken, please give another one :')
        identifiants.append(int(choice2))
        choice3 = input('give a name :')
        server_data['users'].append({'id': id, 'name': choice3})
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
        choice2 = input('give an id :')
        while int(choice2) in identifiants :
            choice2 = input('this id is already taken, please give another one :')
        identifiants.append(int(choice2))
        choice3 = input('give an id :')
        while int(choice3) in identifiants :
            choice3 = input('this id is already taken, please give another one :')
            identifiants.append(int(choice3))
        choice4 = input('give a name :')
        print('-----users id-----')
        for k in range(len(users)):
            print('id :', users[k][0], ', name :', users[k][1])
        print('------------------')
        choice5 = input('give a list of users to add (please give a list of ids) : ')
        server_data['channels'].append({'id': int(choice3), 'name': choice4, 'member_ids': l})
        channels()


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
        print('---group list---')
        for n in g : 
                print(n)
        print('----------------')
        choice1 = input('from which group do you want the messages ? : ')
        if choice1 == 'Town square':
            for n in m :
                print(n)
        menu_input()
        
    elif choice =='g':
        channels()

    else:
        print('Unknown option:', choice)

menu()