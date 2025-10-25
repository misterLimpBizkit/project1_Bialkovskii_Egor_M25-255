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
            if right_answer == 'fat_ginger_cat':
                if 'fat_ginger_cat' in game_state['player_inventory']:
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
        else:
            print('Неверно. Попробуйте снова.')
    return game_state


def attempt_open_treasure(game_state):
    """
    Проверяет есть ли в инвентаре treasure_key,
    если есть - открыввает сундук и игра заканчивается,
    если нет - просит решит загадку, если игрок согласится,

    Args: game_state

    Returns: либо конец игры либо ничего с выводом "Вы отсупаете от сундука"
    """
    inventory = game_state['player_inventory']
    if 'treasure_key' in inventory:
        print("Вы применяете ключ, и замок щёлкает. Сундук открыт!")
        ROOMS[game_state['current_room']]['puzzle'] = None
        print("В сундуке сокровище! Вы победили!")
        game_state['game_over'] = True
    else:
        print("Сундук заперт. Вы можете попробовать взломать его. Ввести код? (да/нет)")
        players_choice = input()
        if players_choice == 'да':
            puzzles_in_the_room = ROOMS[game_state['current_room']]['puzzle']
            players_answer = input(f'{puzzles_in_the_room[0]}:')
            right_answer_treasure_room = puzzles_in_the_room[1]
            if players_answer == right_answer_treasure_room:
                print('Код верный!В сундуке сокровище! Вы победили!')
                ROOMS[game_state['current_room']]['puzzle'] = None
                game_state['game_over'] = True
            else:
                print('Неправильно!')
        else:
            print('Вы отходите от сундука.')
    return game_state

def show_help():
    print("\nДоступные команды:")
    print("  go <direction>  - перейти в направлении (north/south/east/west)")
    print("  look            - осмотреть текущую комнату")
    print("  take <item>     - поднять предмет")
    print("  use <item>      - использовать предмет из инвентаря")
    print("  inventory       - показать инвентарь")
    print("  solve           - попытаться решить загадку в комнате")
    print("  quit            - выйти из игры")
    print("  help            - показать это сообщение")
