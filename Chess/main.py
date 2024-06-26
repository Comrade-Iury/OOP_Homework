from src import Color, Board


def print_board(board: Board):
    print('   +' + '----+' * 8)
    for row in range(8, 0, -1):
        print(f' {row} ', end='')
        for col in range(1, 9):
            print('| ', end='')
            piece = board.get_piece(row, col)
            if piece is None:
                print('  ', end='')
            else:
                print(piece, end='')
            print(' ', end='')
        print('|')
        print('   +' + '----+' * 8)
    print('    ', end='')
    for col in range(8):
        print(f' {chr(65 + col)}   ', end='')
    print()


def convert_step(step: str):
    if len(step) != 2:
        raise Exception('Неверный формат хода')
    s, n = step[0], step[1]
    if ord(s) < ord('A') or ord(s) > ord('H'):
        raise Exception('Неверный формат столбца')
    if ord(n) < ord('1') or ord(n) > ord('8'):
        raise Exception('Неверный формат строки')
    return int(n), ord(s) - ord('A') + 1


def main():
    board = Board()
    while True:
        print_board(board)
        print('Команды:')
        print('    exit                --выход')
        print('    move <from> <to>    --ход из клетки <from> в клетку <to>')
        if board.current_player == Color.WHITE:
            print('Ход белых')
        else:
            print('Ход черных')
        command = input('Введите команду: ')
        if command == 'exit':
            break
        command = command.split()
        if len(command) == 3 and command[0] == 'move':
            try:
                row, col = convert_step(command[1])
                row_1, col_1 = convert_step(command[2])
                if board.move_piece(row, col, row_1, col_1):
                    print('Ход успешен')
                else:
                    print('Неверные координаты. Попробуйте другой ход')
            except Exception as err:
                print('Ошибка:', err)
            finally:
                continue
        print('Неверная команда. Повторите снова')


main()
