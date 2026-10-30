def parse_input(user_input):
    if not user_input.strip():
        return '',

    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    if len(args) != 2:
        return 'Give me a name and phone please.'

    name, phone = args
    contacts[name] = phone
    return 'Contact added.'


def change_contact(args, contacts):
    if len(args) != 2:
        return 'Give me a name and phone please.'

    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return 'Contact updated.'
    return 'Contact not found.'


def show_phone(args, contacts):
    if len(args) != 1:
        return 'Give me a name please.'

    name = args[0]
    if name in contacts:
        return contacts[name]
    return 'Contact not found.'


def show_all(contacts):
    if not contacts:
        return 'No contacts found.'

    return '\n'.join(
        f'{name}: {phone}'
        for name, phone in contacts.items()
    )
def ask_exit():
    while True:
        answer = input(
            'If  you want to exit? (exit/close): '
        ).strip().lower()

        if answer == 'exit':
            return True

        elif answer == 'close':
            return True

        else:
            print('Invalid choice. Please enter exit or close.')

def main():
    contacts = {}
    print('Welcome to the assistant bot!')

    commands = {
        '1': 'add',
        '2': 'change',
        '3': 'phone',
        '4': 'all',
        '5': 'exit'

    }

    while True:

        user_input = user_input = input(
    '\033[32mEnter your message please:\033[0m\n'
    '\033[33mif you want to go out (exit/close): \033[0m'
)

        command, *args = parse_input(user_input)
        command = commands.get(command, command)

        if command in ['close', 'exit']:
            print('Good bye!')
            break
        elif command == 'hello':
            print('How can I help you?')
            print('\nChoose a command:\n'
            '1 - add username phone:\n'
            '2 - change username phone\n'
            '3 - phone username\n'
            '4 - show all contacts\n'
            '5 - Exit/Close\n'
            'Your choice: ')
        elif command == 'add':
            while len(args) != 2:
                args = input('Enter name and phone separated by a space(e.g. Anna +380xxxxxxxxx): ').split()

                if len(args) != 2:
                    print('Invalid input. Enter name and phone separated by a space.')

            print(add_contact(args, contacts))
        elif command == 'change':
            while len(args) != 2:
                args = input('Enter name and phone separated by a space(e.g. Anna +380xxxxxxxxx): ').split()

                if len(args) != 2:
                    print('Invalid input. Enter name and phone separated by a space.')

                print(change_contact(args, contacts))
        elif command == 'phone':
            while len(args) != 1:
                args = input('Enter contact name (e.g. Anna +380xxxxxxxxx): ').split()
                if len(args) != 1:
                    print('Invalid input. Enter contact name and phone separated by a space.')


            print(show_phone(args, contacts))

        elif command == 'all':
            print(show_all(contacts))

        else:
            print('I can help you. Please choose a command.')  # <-- ИЗМЕНИЛИ
            print(  # <-- ДОБАВИЛИ
                '\nChoose a command:\n'
                '1 - add username phone\n'
                '2 - change username phone\n'
                '3 - phone username\n'
                '4 - show all contacts\n'
                '5 - Exit/Close'
            )


if __name__ == '__main__':
    main()
