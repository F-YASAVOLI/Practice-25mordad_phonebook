# """
# Phonebook
#
#
#
#
# """
#
#
# import os
#
# contact_dict = {
#         '0915233' : {'name' : 'Reyhane' , 'family' : 'Fallah' , 'E_mail' : 'reyhaneh@gmail.com'},
#         '0996679' : {'name' : 'Fatemeh' , 'family' : 'Yasavoli' , 'E_mail' : 'fatemeh@gmail.com'},
#         '0915819' : {'name' : 'Azam' , 'family' : 'Bahrami' , 'E_mail' : 'azam@gmail.com'},
#         '0915581' : {'name' : 'Mohsen' , 'family' : 'Barati' , 'E_mail' : 'mohsen@gmail.com'},
#         '0901905' : {'name' : 'Amir' , 'family' : 'Navaee' , 'E_mail' : 'amir@gmail.com'}
#         }
#
#
# def add_update_contact():
#     global contact_dict
#     number = int(input('\ninsert contact number: '))
#     name = input('insert contact name: ')
#     family = input('insert contact family: ')
#     E_mail = input('insert contact E_mail: ')
#
#     contact_dict[number] = {'Name' : name, 'Family' : family, 'E_mail' : E_mail}
#
#
# def delete_contact():
#     global contact_dict
#     number = int(input('insert contact number: '))
#     if number in contact_dict:
#         contact_dict.pop(number)
#     else:
#         print('Number not exist!')
#
#
# def search_contact():
#     global cantact_dict
#     os.system('cls')
#     number = int(input('insert contact number: '))
#     if number in cantact_dict:
#         print('Number : ', number, '|',
#               'Name : ', cantact_dict[number]['name'], '|',
#               'Family : ', contact_dict[number]['family'], '|',
#               'E-mail : ', contact_dict[number]['E_mail'],
#               sep='\n')
#
#
# def show_all_contact():
#     global cantact_dict
#
#     for number in cantact_dict:
#         print('Number : ',number,'|',
#         'Name : ',cantact_dict[number]['name'],'|',
#         'Family : ',contact_dict[number]['family'],'|',
#         'E-mail : ',contact_dict[number]['E_mail'],
#         sep = '\n')
#
#
#
# def exit():
#     exit()
# while True:
#     def meno():
#         print('_'*25,
#             ' Welcome to Phonebook!!!',
#              '_'*25,'\n',
#             'Meno Contact:',
#             '1- add or edit contact',
#             '2- delete contact',
#             '3- search contact',
#             '4- show all cantact',
#             '5- exit',
#             sep = '\n')
#
#         choose = int(input('\nChoose one of the following options: '))
#
#         if choose == 1:
#             add_update_contact()
#         elif choose == 2:
#             delete_contact()
#         elif choose == 3:
#             search_contact()
#         elif choose == 4:
#             show_all_contact()
#         elif choose == 5:
#             exit()
#         else:
#             print('Wrong Option!! Try again.')
#     os.system('cls')
#     meno()















#
# import os
#
# contact_dict = {
#     '0915233': {'name': 'Reyhane', 'family': 'Fallah', 'E_mail': 'reyhaneh@gmail.com'},
#     '0996679': {'name': 'Fatemeh', 'family': 'Yasavoli', 'E_mail': 'fatemeh@gmail.com'},
#     '0915819': {'name': 'Azam', 'family': 'Bahrami', 'E_mail': 'azam@gmail.com'},
#     '0915581': {'name': 'Mohsen', 'family': 'Barati', 'E_mail': 'mohsen@gmail.com'},
#     '0901905': {'name': 'Amir', 'family': 'Navaee', 'E_mail': 'amir@gmail.com'}
# }
#
#
# def add_update_contact():
#     global contact_dict
#
#     number = input('\nInsert contact number: ')
#
#
#     if number in contact_dict:
#         print('This number is already in your contacts.')
#
#         answer = input('Do you want to update this contact? (yes/no): ')
#
#         if answer.lower() != 'yes' or 'y':
#             print('Nothing changed.')
#             return
#
#     name = input('Insert contact name: ')
#     family = input('Insert contact family: ')
#     E_mail = input('Insert contact E_mail: ')
#
#     contact_dict[number] = {
#         'name': name,
#         'family': family,
#         'E_mail': E_mail
#     }
#
#     print('Contact saved successfully!')
#
#
# def delete_contact():
#     global contact_dict
#
#     number = input('Insert contact number: ')
#
#     if number in contact_dict:
#
#         print('Name:', contact_dict[number]['name'])
#         print('Family:', contact_dict[number]['family'])
#
#         answer = input('Are you sure you want to delete this contact? (yes/no): ')
#
#         if answer.lower() == 'yes' or 'y':
#             contact_dict.pop(number)
#             print('Contact deleted successfully!')
#         else:
#             print('Nothing changed.')
#
#     else:
#         print('Number does not exist!')
#
#
# def search_contact():
#     number = input('Insert contact number: ')
#
#     if number in contact_dict:
#         print(
#             'Number:', number,
#             '\nName:', contact_dict[number]['name'],
#             '\nFamily:', contact_dict[number]['family'],
#             '\nE-mail:', contact_dict[number]['E_mail']
#         )
#     else:
#         print('Number does not exist!')
#
#
# def show_all_contact():
#
#     for number in contact_dict:
#         print(
#             'Number:', number,
#             '\nName:', contact_dict[number]['name'],
#             '\nFamily:', contact_dict[number]['family'],
#             '\nE-mail:', contact_dict[number]['E_mail'],
#             '\n','-'*40
#         )
#
#
# def menu():
#     print(
#         '\n','_' * 25,
#         'Welcome to Phonebook!!!',
#         '_' * 25,
#         '\n')
#     while True:
#
#         print(
#             '\nMenu Contact:',
#             '1- Add or edit contact',
#             '2- Delete contact',
#             '3- Search contact',
#             '4- Show all contacts',
#             '5- Exit',
#             sep='\n'
#         )
#
#         choose = input('\nChoose one of the following options: ')
#         print('_'*40,'\n')
#
#         if choose == '1':
#             add_update_contact()
#
#         elif choose == '2':
#             delete_contact()
#
#         elif choose == '3':
#             search_contact()
#
#         elif choose == '4':
#             show_all_contact()
#
#         elif choose == '5':
#             print('Goodbye!')
#             return False
#
#         else:
#             print('Wrong Option!! Try again.')
#
#
#
#
#
#
# os.system('cls')
#
# menu()










"""
program name : Phonebook
programer name : Fateme Yasavoli
email : fatemeyasavoli900@gmail.com
"""
import os

contact_dict = {
    '0915233': {'name': 'Reyhane', 'family': 'Fallah', 'E_mail': 'reyhaneh@gmail.com'},
    '0996679': {'name': 'Fatemeh', 'family': 'Yasavoli', 'E_mail': 'fatemeh@gmail.com'},
    '0915819': {'name': 'Azam', 'family': 'Bahrami', 'E_mail': 'azam@gmail.com'},
    '0915581': {'name': 'Mohsen', 'family': 'Barati', 'E_mail': 'mohsen@gmail.com'},
    '0901905': {'name': 'Amir', 'family': 'Navaee', 'E_mail': 'amir@gmail.com'}
}


def add_update_contact():
    global contact_dict

    print('=' * 40)
    print('        ADD / UPDATE CONTACT')
    print('=' * 40)

    number = input('\nInsert contact number: ')

    if number in contact_dict:
        print('\nThis number is already in your contacts.')

        answer = input('Do you want to update this contact? (yes/no): ')

        if answer.lower() not in ('yes', 'y'):
            print('Nothing changed.')
            return

    name = input('Insert contact name: ')
    family = input('Insert contact family: ')
    E_mail = input('Insert contact E_mail: ')

    contact_dict[number] = {
        'name': name,
        'family': family,
        'E_mail': E_mail
    }

    print('\nContact saved successfully!')


def delete_contact():
    global contact_dict

    print('=' * 40)
    print('           DELETE CONTACT')
    print('=' * 40)

    number = input('\nInsert contact number: ')

    if number in contact_dict:

        print('\nName:', contact_dict[number]['name'])
        print('Family:', contact_dict[number]['family'])

        answer = input(
            '\nAre you sure you want to delete this contact? (yes/no): '
        )

        if answer.lower() in ('yes', 'y'):
            contact_dict.pop(number)
            print('\nContact deleted successfully!')
        else:
            print('\nNothing changed.')

    else:
        print('\nNumber does not exist!')


def search_contact():

    print('=' * 40)
    print('            SEARCH CONTACT')
    print('=' * 40)

    number = input('\nInsert contact number: ')

    if number in contact_dict:
        print(
            '\nNumber:', number,
            '\nName:', contact_dict[number]['name'],
            '\nFamily:', contact_dict[number]['family'],
            '\nE-mail:', contact_dict[number]['E_mail']
        )
    else:
        print('\nNumber does not exist!')


def show_all_contact():

    print('=' * 40)
    print('          ALL CONTACTS')
    print('=' * 40)

    if len(contact_dict) == 0:
        print('\nContact list is empty!')
        return

    for number in contact_dict:
        print(
            '\nNumber:', number,
            '\nName:', contact_dict[number]['name'],
            '\nFamily:', contact_dict[number]['family'],
            '\nE-mail:', contact_dict[number]['E_mail'],
            '\n', '-' * 40
        )


def menu():
    print(
        '\n','_' * 25,
        'Welcome to Phonebook!!!',
        '_' * 25,
        '\n')

    print(
        '\nMenu Contact:',
        '1- Add or edit contact',
        '2- Delete contact',
        '3- Search contact',
        '4- Show all contacts',
        '5- Exit',
        sep='\n'
    )

    choose = input('\nChoose one of the following options: ')


    os.system('cls')

    if choose == '1':
        add_update_contact()

    elif choose == '2':
        delete_contact()

    elif choose == '3':
        search_contact()

    elif choose == '4':
        show_all_contact()

    elif choose == '5':
        print('Goodbye!')
        return False

    else:
        print('Wrong Option!! Try again.')

    return True


while True:

    os.system('cls')


    result = menu()


    if result is False:
        break

    print('\n')
    answer = input('Do you want to do another operation? (yes/no): ')

    if answer.lower() not in ('yes', 'y'):
        print('\nGoodbye!')
        break
