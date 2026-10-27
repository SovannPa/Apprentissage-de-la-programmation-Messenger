from datetime import datetime

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

u = []
for d in server_data['users']:
    u.append(d['name'])

g = []
for d in server_data['channels']:
    g.append(d['name'])

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
    u = []
    identifiants = []
    print('---------option---------')
    print('print users : p')
    print('add user : a')
    print('back to the main menu : b')
    print('------------------------')
    for d in server_data['users']:
        u.append(d['name'])
        identifiants.append(d['id'])
    choice = input('what do you want to do ? :')
    if choice == 'p' :
        print('------users list------')
        for n in u :
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
        for n in g :
            print(n)
        menu_input()
    else:
        print('Unknown option:', choice)

menu()