#!/usr/bin/env python3
from labyrinth_game.constants import ROOMS
from labyrinth_game.utils import describe_current_room 
from labyrinth_game.player_actions import get_input, show_inventory

#Создаем словарь с состоянием игры
game_state = {
    'player_inventory': [], # Инвентарь игрока
    'current_room': 'entrance', # Текущая комната
    'game_over': False, # Значения окончания игры
    'steps_taken': 0 # Количество шагов
}

#Utils.py проба фунцкий
def describe_current_room(game_state):
    """
    Выводит название комнаты, следом описание, список предметов,
    доступные выходы и сообщение о наличии загадокю

    Args: словарь game_state

    Returns: все свойства комнаты
    """
    current_room_name = game_state['current_room']
    print(f'{current_room_name.upper():=^75}')
    print(ROOMS[current_room_name]['description'])
    if ROOMS[current_room_name]['items'] == []:
        print('В комнате нет ничего полезного.')
    else:
        print(f'Заметные предметы: {', '.join(ROOMS[current_room_name]['items'])}')
    print(f'Выходы: {', '.join(ROOMS[current_room_name]['exits'])}')
    if ROOMS[current_room_name]['puzzle']:
        print("Кажется, здесь есть загадка (используйте команду solve).")
    print('='*75)

#describe_current_room(game_state)

#player_actions.py проба функций
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

#show_inventory(game_state)

def get_input(prompt="> "):
    """
    Безопасный ввод данных от пользователя с обработкой ошибок
    
    Args:
        prompt (str): Текст приглашения для ввода
    
    Returns:
        str: Введенная пользователем строка или "quit" при прерывании
    """
    try:
        return input(prompt)
    except (KeyboardInterrupt, EOFError):
        print("\nВыход из игры.")
        return "quit"
    
#get_input()

def move_player(game_state, direction):
    """
    Двигает игрока по карте и меняет состояние game_state

    Args: состояние игры и направление следующего шага

    Returns: комната в состоянии игры обновляется, шаг увеличивается на единицу и выводится описание новой комнаты 
    """
    current_room_name = game_state['current_room']
    current_room_exits = ROOMS[current_room_name]['exits']
    if direction in list(current_room_exits):
        new_room_name = current_room_exits[direction] 
        game_state['current_room'] = new_room_name
        game_state['steps_taken'] = game_state.get('steps_taken', 0) + 1 #можно += 1, т.к. steps_taken заранее инициирован
        print(f'Вы переместились {direction} в {new_room_name}!\n')
        describe_current_room(game_state)
    else:
        print('Нельзя пойти в этом направлении.')

    return game_state


#move_player(game_state, 'north')
#print(game_state)

def process_command(game_state, item_name):
    """
    Добавляет выбранный предмет в инвентарь 

    Args: состояние инввентаря и вещи в комнате - все в game_state

    Returns: изменненый game_state, а именно инвентарь
    """
    items_in_the_room = ROOMS[game_state['current_room']]['items']
    if item_name in list(items_in_the_room):
        game_state['player_inventory'].append(item_name)
        print(f'Вы подняли: {item_name}')
        items_in_the_room.remove(item_name)
    else:
        print("Такого предмета здесь нет.")
    
    return game_state

process_command(game_state, 'torch')
print(game_state)
print(ROOMS)

