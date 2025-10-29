#!/usr/bin/env python3
#Импорт словаря комнат
from labyrinth_game.player_actions import (
    get_input,
    move_player,
    show_inventory,
    take_item,
    use_item,
)
from labyrinth_game.utils import (
    attempt_open_treasure,
    describe_current_room,
    show_help,
    solve_puzzle,
)

#Создаем словарь с состоянием игры
game_state = {
    'player_inventory': [], # Инвентарь игрока
    'current_room': 'entrance', # Текущая комната
    'game_over': False, # Значения окончания игры
    'steps_taken': 0 # Количество шагов
}

def process_command(game_state, command):
    '''
    Обрабатывает команды, введенные игроком

    Args: game_state и комманда из инпута игрока

    Returns: вызов функции и выполнение действия
    '''
    separation = command.split()
    
    action = separation[0]

    directions = ['north', 'south', 'east', 'west']
    if action in directions:
        move_player(game_state, action)
        return game_state['game_over']

    match action:
        case 'look':
            describe_current_room(game_state)
        case 'solve':
            if game_state['current_room'] == 'treasure_room':
                attempt_open_treasure(game_state)
            else:
                solve_puzzle(game_state)
        case 'use':
            item_name = separation[1]
            use_item(game_state, item_name)
        case 'go':
            if len(separation) < 2:
                print('Попробуй объединить с направлением. Например, go north')
            else:
                direction = separation[1]
                move_player(game_state, direction)
        case 'take':
            if len(separation) < 2:
                print('Попробуй объединить с предметом. Например, take torch')
            else:
                item_name = separation[1]
                take_item(game_state, item_name)
        case 'inventory':
            show_inventory(game_state)
        case 'quit':
            print('Игра окончена')
            game_state['game_over'] = True
        case 'help':
            show_help()
        case _:
            print('Такой команды нет.')
            show_help()
        
    return game_state['game_over']
            



def main():
    print('Добро пожаловать в Лабиринт сокровищ!\n')
    describe_current_room(game_state)
    while not game_state['game_over']:
        current_command = get_input()
        process_command(game_state, current_command)

if __name__ == '__main__':
    main()