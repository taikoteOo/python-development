# import utils - импорт всего файла
# обращаться через utils.bye

# from utils import * - импортирует всё из файла
# from utils import print_name, bye, text
#
# def main():
#     print_name(text)
#     bye()
#
# main()

import utils
def main():
    utils.print_name('Alex')
    utils.bye()

main()