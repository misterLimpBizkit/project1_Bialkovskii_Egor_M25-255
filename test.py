from labyrinth_game.constants import ROOMS

#Создаем словарь с состоянием игры
game_state = {
    'player_inventory': [], # Инвентарь игрока
    'current_room': 'entrance', # Текущая комната
    'game_over': False, # Значения окончания игры
    'steps_taken': 0 # Количество шагов
}

#Utils.py проба фунцкии
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
        print('В комнате нет ничего полезного.')
    else:
        print(f'Заметные предметы: {', '.join(ROOMS[the_room]['items'])}')
    print(f'Выходы: {', '.join(ROOMS[the_room]['exits'])}')
    if ROOMS[the_room]['puzzle']:
        print("Кажется, здесь есть загадка (используйте команду solve).")
    print('='*75)

#describe_current_room(game_state)

#player_actions.py
def show_inventory(game_state):
    """
    Выводит содержимое инвенторя

    Args: словарь game_state

    Returns: game_state['player_inventory']
    """
    if game_state['player_inventory']:
        print(f'В вашем инвантаре: {", ".join(game_state['player_inventory'])}')
    else:
        print('У вас пустой инвентарь.')

show_inventory(game_state)