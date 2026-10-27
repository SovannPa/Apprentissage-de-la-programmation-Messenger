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

l1 = server_data['users']
u = []
for d in l1 :
    u.append(d['name'])

g = []
for d in server_data['channels']:
    g.append(d['name'])

m = []
for d in server_data['messages']:
    m.append(d['content'])


print('=== Messenger ===')
print('x. Leave')
choice = input('Select an option between u, m, g, x :')
if choice == 'x':
    print('Bye!')
elif choice =='u':
    for n in u :
        print(n)
elif choice =='m':
    for n in m :
        print(n)
elif choice =='g':
    for n in g :
        print(n)
    
else:
    print('Unknown option:', choice)
