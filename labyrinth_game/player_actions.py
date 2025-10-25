from labyrinth_game.constants import ROOMS
from labyrinth_game.utils import describe_current_room 

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
        print(f'Такого направления нет, попробуй: {', '.join(current_room_exits)}')

    return game_state

def take_item(game_state, item_name):
    """
    Добавляет выбранный предмет в инвентарь 

    Args: состояние инвентаря и вещи в комнате - все в game_state

    Returns: измененный game_state, а именно инвентарь
    """
    items_in_the_room = ROOMS[game_state['current_room']]['items']
    if item_name == 'treasure_chest':
        print('Вы не можете поднять сундук, он слишком тяжелый.')
    elif item_name in items_in_the_room:
        game_state['player_inventory'].append(item_name)
        items_in_the_room.remove(item_name)
        print(f'Вы подняли: {item_name}')  
    else:
        print("Такого предмета здесь нет.")
    
    return game_state

def use_item(game_state, item_name):
    """
    Использует предмет из инвентаря

    Args: game_state и название предмета

    Returns: действие, вызванное использованием предмета
    """
    my_items = game_state['player_inventory']
    if item_name in my_items:
        match item_name:
            case 'torch':
                print('Вы достали факел. В комнате стало заметно светлее.')
            case 'sword':
                print('Вы достали меч. Ваша уверенность в себе резко подскачила.')
            case 'bronze_box':
                print('Вы открыли шкатулку. Внутри старый, ржавый ключ.')
                game_state['player_inventory'].append('rusty_key')
            case 'ginger car':
                print('Мяу')
            case 'black kitten':
                print('МИУ миу')
            case 'fat ginger cat':
                print('МЯЯЯЯУ')
            case 'Священный алмаз':
                print('Алмаз красиво сверкает, вам это нравится')
            case 'treasure_room_key':
                print('Вам это еще пригодится')
            case _:
                print('Непонятно как это использовать')

    return game_state