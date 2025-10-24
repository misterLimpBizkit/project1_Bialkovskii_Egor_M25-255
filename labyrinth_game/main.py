#!/usr/bin/env python3
#Импорт словаря комнат
from labyrinth_game.constants import ROOMS
from labyrinth_game.utils import describe_current_room, solve_puzzle 
from labyrinth_game.player_actions import get_input, show_inventory, move_player, take_item, use_item

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

    if not separation:
        print('Такой команды нет.')
    

    action = separation[0]

    list_of_options = ('look', 'use', 'go', 'take', 'inventory', 'quit')

    match action:
        case 'look':
            describe_current_room(game_state)
        case 'solve':
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
                print('Попробуй объединить с направлением. Например, go north')
            else:
                item_name = separation[1]
                take_item(game_state, item_name)
        case 'inventory':
            show_inventory(game_state)
        case 'quit':
            print('Игра окончена')
            game_state['game_over'] = True
        case _:
            print(f'Такой команды нет. Попробуй: \n{'\n'.join(list_of_options)}')
        
    return game_state['game_over']
            



def main():
    print('Добро пожаловать в Лабиринт сокровищ!\n')
    describe_current_room(game_state)
    while game_state['game_over'] == False:
        current_command = get_input()
        process_command(game_state, current_command)

if __name__ == '__main__':
    main()