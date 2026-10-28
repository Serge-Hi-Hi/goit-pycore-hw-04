
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
    name = name.lower()

    if name in contacts:
        return 'Contact already exists.'

    contacts[name] = phone
    return 'Contact added.'


def change_contact(args, contacts):
    if len(args) != 2:
        return 'Give me a name and phone please.'

    name, phone = args
    name = name.lower()

    if name in contacts:
        contacts[name] = phone
        return 'Contact updated.'

    return 'Contact not found.'


def show_phone(args, contacts):
    if len(args) != 1:
        return 'Give me a name please.'

    name = args[0].lower()

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


def delete_contact(args, contacts):
    if len(args) != 1:
        return 'Give me a name please.'

    name = args[0].lower()

    if name in contacts:
        del contacts[name]
        return 'Contact deleted.'

    return 'Contact not found.'


def search_contacts(query, contacts):
    query = query.lower()

    results = []

    for name, phone in contacts.items():
        if query in name:
            results.append(f'{name.capitalize()}: {phone}')

    if not results:
        return 'No matching contacts found.'

    return '\n'.join(results)



def ask_exit():
    while True:
        answer = input(
            'Do you want to exit? (yes/no): '
        ).strip().lower()

        if answer == 'yes':
            return True

        elif answer == 'no':
            return False

        else:
            print('Invalid choice. Please enter yes or no.')



def main():
    contacts = {}
    password = '1234'

    print('Welcome to the assistant bot!')

    commands = {
        '1': 'add',
        '2': 'change',
        '3': 'phone',
        '4': 'all',
        '5': 'delete',
        '6': 'search',
        '7': 'exit'
    }

    while True:
        user_input = input(
            '\nChoose a command:\n'
            '1 - Add contact\n'
            '2 - Change phone number\n'
            '3 - Show phone number\n'
            '4 - Show all contacts\n'
            '5 - Delete contact\n'
            '6 - Search contacts\n'
            '7 - Exit\n'
            'Your choice: '
        )

        command, *args = parse_input(user_input)
        command = commands.get(command, command)

        if command in ['close', 'exit']:
            print('Good bye!')
            break

        elif command == 'hello':
            print('How can I help you?')

        elif command == 'add':
            name = input(
                'Enter contact name (e.g. Anna): ').strip()

            if not name:
                print('Invalid name. Please enter a contact name.')
                continue

            attempts = 0

            while attempts < 3:
                phone = input(
                    'Enter your phone number (+380XXXXXXXXX): '
                ).strip()

                if not (
                    phone.startswith('+380')
                    and len(phone) == 13
                    and phone[1:].isdigit()
                ):
                    attempts += 1
                    print(
                        'Invalid phone number. '
                        'Please enter a valid number (+380XXXXXXXXX).'
                    )
                    continue

                break

            if attempts == 3:
                print('Too many attempts. Returning to main menu.')
                continue

            print(add_contact([name, phone], contacts))
            if ask_exit():
                print('Good bye!')
                break

        elif command == 'change':

            name_attempts = 0

            while name_attempts < 3:
                name = input(
                    'Enter contact name (e.g. Anna): '
                ).strip().lower()

                if not name:
                    print('Invalid name. Please enter a contact name.')
                    name_attempts += 1
                    continue

                if name not in contacts:
                    print('Contact not found.')
                    name_attempts += 1
                    continue

                break

            if name_attempts == 3:
                print('Too many attempts. Returning to main menu.')
                continue

            attempts = 0

            while attempts < 3:
                phone = input(
                    'Enter new phone number (+380XXXXXXXXX): '
                ).strip()

                if not (
                    phone.startswith('+380')
                    and len(phone) == 13
                    and phone[1:].isdigit()
                ):
                    attempts += 1
                    print(
                        'Invalid phone number. '
                        'Please enter a valid number (+380XXXXXXXXX).'
                    )
                    continue

                break

            if attempts == 3:
                print('Too many attempts. Returning to main menu.')
                continue

            print(change_contact([name, phone], contacts))
            if ask_exit():
                print('Good bye!')
                break

        elif command == 'phone':
            name_attempts = 0
            while name_attempts < 3:
                name = input('Enter contact name (e.g. Anna): ').strip().lower()
                if not name:
                    print('Invalid name. Please enter a contact name:')
                    name_attempts += 1
                    continue
                if name not in contacts:
                    print('Contact not found.')
                    name_attempts += 1
                    continue

                break
            if name_attempts == 3:
                print('Too many attempts. Returning to main menu.')
                continue
            print(show_phone([name], contacts))
            if ask_exit():
                print('Good bye!')
                break

        elif command == 'all':
            attempts = 0
            while attempts < 3:
                name = input('Enter password(must be 4 Numbers, for Example: 1111): ').strip()
                if name == password:
                    print('Password is valid.')
                    print(show_all(contacts))
                    break
                attempts += 1
                print('Invalid password.')

            if attempts == 3:
                print('Too many attempts. Returning to main menu.')
            if ask_exit():
                print('Good bye!')
                break

        elif command == 'delete':
            name_attempts = 0
            while name_attempts < 3:
                name = input('Enter contact name (e.g. Anna): ').strip().lower()


                if not name:
                    print('Invalid name. Please enter a contact name.')
                    continue

                if name not in contacts:
                    print('Contact not found.')
                    name_attempts += 1
                    continue

                break
            if name_attempts == 3:
                print('Too many attempts. Returning to main menu.')
                continue



            confirmation = input('Are you sure you want to delete this contact? (yes/no): ').strip().lower()

            if confirmation == 'yes':
                print(delete_contact([name], contacts))
            else:
                print('Deletion cancelled.')

        elif command == 'search':
            while True:
                query = input('Enter name to search (or back): ').strip().lower()

                if query == 'back':
                    print('Returning to main menu...')
                    break

                if not query:
                    print('Invalid search. Please enter a name.')
                    continue

                print(search_contacts(query, contacts))
            if ask_exit():
                print('Good bye!')
                break


if __name__ == '__main__':
    main()
