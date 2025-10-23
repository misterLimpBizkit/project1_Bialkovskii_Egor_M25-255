from labyrinth_game.constants import ROOMS

def describe_current_room(game_state):
    """
    Выводит название комнаты, следом описание, список предметов,
    доступные выходы и сообщение о наличии загадокю

    Args: словарь game_state

    Returns: все свойства комнаты
    """
    the_room = game_state['current_room']
    print(f'{the_room.upper():=^75}')
    print(ROOMS[the_room]['description'])
    if ROOMS[the_room]['items'] == []:
        print('В комнате нет ничего полезного')
    else:
        print(f'Заметные предметы: {', '.join(ROOMS[the_room]['items'])}')
    print(f'Выходы: {', '.join(ROOMS[the_room]['exits'])}')
    if ROOMS[the_room]['puzzle']:
        print("Кажется, здесь есть загадка (используйте команду solve).")
    print('='*75)



