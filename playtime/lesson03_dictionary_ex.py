
#dictionary + key info
contacts = {
'Shannon': {'phone': '202-555-1234',
'twitter': '@svt827', 'github':
'@shannonturner' },

'Anupama': {'phone': '410-333-9876',
'twitter': '@iamtheanupama', 'github':
'@apillalamarri'}
}

#loop through that dictionary to display everyone's contact information:

#people = shannon, anupama
#info = the dictionary that coordinates with shannon and anupama
#values within dict = phone, twitter, github
for people, info in contacts.items():
    print people + "'s contact information is: \n" + "Phone:" + info.get('phone') + "\nTwitter:" + info.get('twitter') + "\nGithub:" + info.get('github')
















