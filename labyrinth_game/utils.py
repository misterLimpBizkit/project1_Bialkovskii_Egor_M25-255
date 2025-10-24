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


def solve_puzzle(game_state):
    """
    Проверяет есть ли в комнтае загадка, если есть - просит игрока решить ее

    Args: game_state

    Returns: дает игроку награду и убирает загадку из комнтаы
    """
    puzzles_in_the_room = ROOMS[game_state['current_room']]['puzzle']
    right_answer = puzzles_in_the_room[1]
    question = puzzles_in_the_room[0]
    if puzzles_in_the_room:
        print(question)
        answer = input('Ваш ответ:')
        if answer == right_answer:
            if right_answer == 'fat ginger cat':
                if 'fat ginger cat' in game_state['player_inventory']:
                    print('Правильно')
                    print(f'Вы получаете: {puzzles_in_the_room[2]}!')
                    ROOMS[game_state['current_room']]['puzzle'] = None
                else:
                    print('У вас нет толстого кота, подберите его.')
            else:
                print('Правильно')
                print(f'Вы получаете: {puzzles_in_the_room[2]}!')
                game_state['player_inventory'].append(puzzles_in_the_room[2])
                ROOMS[game_state['current_room']]['puzzle'] = None
    return game_state
