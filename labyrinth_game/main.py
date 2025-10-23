#!/usr/bin/env python3
#Импорт словаря комнат
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

def main():
    print('Добро пожаловать в Лабиринт сокровищ!\n')
    describe_current_room(game_state)
    while game_state['game_over'] == False:
        get_input()

if __name__ == '__main__':
    main()