import time



dict_users = [
    {'name': 'Vlad', 'tel': '0959500000'},
    {'name': 'Nika', 'tel': '0959500001'}
]


def input_error(func_command):
    def wrapper(*args):
    #     # type command >>> add Bill 0675432323
        try:
            return func_command(*args)
        except IndexError:
            print('\nSorry, unknown 1111111 command. Try again!')
        # except TypeError:
        #     print('Sorry, unknown TypeError command. Try again!')
        # except KeyError:
        #     print('Sorry, unknown KeyError command. Try again!')
        except ValueError:
            print('\nSorry, unknown ValueError command. Try again!')
        # except TypeError:
        #     print('Sorry, unknown TypeError command. Try again!')
        # finally:
        #     print('пользователь вводит имя и номер телефона, обязательно через пробел')   
    return wrapper

    
def hello(*args):
    """Bot say ))) """
    return ('\nbot >>> How can I help you?')

@input_error
def add(*args):
    """add NEW user and phonenumber"""
    name_user = args[0].title()
    phone_user = int(args[1])
    new_user = {'name': name_user, 'tel': phone_user}
    dict_users.append(new_user)
    print(new_user)
    return (f"\nThis command is ADD, name {name_user}, phone-number {phone_user}")


@input_error
def change(*args):
    """change phonenumber for thisone user """
    name_user = args[0].title()
    phone_user = int(args[1])
    for user in dict_users:
        if name_user == user['name']:
            user['tel'] = phone_user
            print(user)
    return (f"\nThis command is CHANGE, name {name_user}, NEW phone-number {phone_user}")


@input_error
def phone(*args):
    """show thisone user and phonenumber"""
    name_user = args[0].title()
    for user in dict_users:
        if name_user == user['name']:
            print(f"User with name {name_user} have phone-number - {user['tel']}")
            print(user)
    return (f"\nThis command is PHONE, name {name_user}, phone-number {user['tel']}")


def show_all(*args):
    """show all users and phonenumbers"""
    print('Ok! I show you all of I know.\nEnter password\n\n')
    # time.sleep(3)
    for user in dict_users:
        print(f"\nUser name: {user['name']}  - phone number: {user['tel']}")


def save_phonebook(*args):
    pass

    
@input_error    
def command_parser(user_input: str):
    """passer user enter command"""
    for command, keyword in COMMANDS.items():                   #
        if user_input.startswith(keyword):
            return command, user_input.replace(keyword, "").strip().split(" ")
            #                                                                      retuurn COMMANDS(user_input[0])
    return None, None

@input_error
def main():
    """bot for phonenumber's book"""
    while True:
        print('\nBot waiting ...')
        user_input = input('type command >>> ').lower()
        print('input done ... ', str(user_input))
        if user_input == ".":
            time.sleep(1)
            print("\nI'll back!\n\n")
            time.sleep(1)
            break
        command, data = command_parser(user_input)
        if not command:
            time.sleep(1)
            print('\nSorry, unknown command. Try again!\n\n')
            continue


        print(command(*data))
        
    

COMMANDS = {
    add: 'add',
    hello: 'hello',
    change: 'change',
    phone: 'phone',
    show_all: 'show_all',
    save_phonebook: 'save'
}

if __name__ == '__main__':
    main()

