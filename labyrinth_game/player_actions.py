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