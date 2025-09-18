cmd = 'top'

match cmd:
    case 'top' | 'start':
        print('top command')
    case 'bottom':
        print('bottom command')
    case _:
        print('other command')


match cmd:
    case str() as command:  # checks if cmd is of type str
        print(f'string  {command}')