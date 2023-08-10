def get_user_entry():
    command = input("Command: ")
    return command


def dispatch_command(command):
    match command:
        case "create":
            print("creation d un inventaire")
        case _:
            print("Commande inconnue")


if __name__ == '__main__':
    while True:
        dispatch_command(get_user_entry())

