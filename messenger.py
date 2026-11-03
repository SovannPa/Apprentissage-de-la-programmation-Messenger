from datetime import datetime
from ast import literal_eval
import random as rd
import json

###############################################################################----JSON----############################################################################
def load_server_data_from_file():
    return json.load(open('storage.json'))

server_data = load_server_data_from_file()

def serialisation():
    JSON_FILE_NAME = 'storage.json'
    with open(JSON_FILE_NAME, 'w') as json_file:
        json.dump(server_data, json_file)

#######################################################################################################################################################################

def print_users(user_ids=None):
    print('--------users list--------')
    for d in server_data['users']:
        if user_ids is None or d['id'] in user_ids:
            print('id :', d['id'], ', name :', d['name'])
    print('--------------------------')

def print_channels():
    print('--------channels--------')
    for d in server_data['channels']:
        print('id :', d['id'], ', name :', d['name'])
    print('------------------------')

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
        print_users()
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
        serialisation()
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
        print_channels()
        channels()

    elif choice == 'b':
        menu()

    elif choice == 'a':
        id = rd.randint(0, 1000)
        while id in identifiants :
            id = rd.randint(0, 1000)
        identifiants.append(id)
        choice3 = input('give a name :')
        print_users()
        choice4 = input('give a list of users to add (please give a list of ids) : ')
        server_data['channels'].append({'id': id, 'name': choice3, 'member_ids': literal_eval(choice4)})
        serialisation()
        channels()

        

def messages():

    print('---------option---------')
    print('print messages of a group : p')
    print('send message : s')
    print('back to the main menu : b')
    print('------------------------')

    choice = input('what do you want to do ? :')

    if choice == 'p':
        identifiants = [d['id'] for d in server_data['channels']]
        print_channels()
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
            date = datetime.fromisoformat(d['reception_date'])
            if date.date() != day:
                day = date.date()
                print('------', day.strftime('%d/%m/%Y'), '------')
            sender = names.get(d['sender_id'], 'Unknown')
            print(date.strftime('%H:%M:%S'), '|', sender, ':', d['content'])
        print('------------------')
        messages()

    elif choice == 'b':
        menu()

    elif choice =='s':
        print_channels()
        choice2 = input('in which group ? (id) :')
        channel_ids = [d['id'] for d in server_data['channels']]
        if not choice2.isdigit() or int(choice2) not in channel_ids:
            print('Unknown group:', choice2)
            messages()
            return
        channel = next(d for d in server_data['channels'] if d['id'] == int(choice2))
        print_users(channel['member_ids'])
        choice3 = input('who are you ? (id) : ')
        choice4 = input('type :')
        identifiants = []
        for d in server_data['messages']:
            identifiants.append(d['id'])
        id = id = rd.randint(0, 1000)
        while id in identifiants:
            id = rd.randint(0, 1000)
        server_data['messages'].append({"id": id, "reception_date": datetime.now().isoformat(timespec='seconds'), "sender_id": int(choice3), "channel": int(choice2), "content": choice4})
        serialisation()
        messages()


        
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