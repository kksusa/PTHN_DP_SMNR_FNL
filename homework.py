import os
from collections import namedtuple
import logging
import argparse

FORMAT = '{levelname} - {asctime} {msg} '
logging.basicConfig(format=FORMAT, style="{", filename="dir_log.log", filemode='w', encoding="utf-8",
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def object_logging(cur_tuple):
    return logger.info(
        f"Имя объекта: {cur_tuple.name}, расширение: {cur_tuple.extension}, папка: {cur_tuple.dir_flag}, "
        f"родительский каталог: {cur_tuple.parent_dir}")


def request_dir():
    while True:
        requested_dir = input("Введите путь до требуемой директории. "
                              "Для использования текущей директории оставьте поле пустым: ")
        if requested_dir == "":
            requested_dir = os.getcwd()
            break
        elif not os.path.exists(requested_dir):
            print("Такого пути нет. Попробуйте снова.")
        elif os.path.isfile(requested_dir):
            print("Это путь к файлу, а не директории. Попробуйте снова.")
        else:
            break
    tuple_gen(requested_dir)


def tuple_gen(requested_dir):
    DirObject = namedtuple('DirObject', ['name', 'extension', 'dir_flag', 'parent_dir'])
    par_dir = requested_dir.split("\\")[-1]
    dir_list = os.listdir(requested_dir)
    for i in dir_list:
        if os.path.isfile(i):
            temp = os.path.splitext(i)
            obj_name = temp[0]
            ext = temp[1]
            flag = False
        else:
            obj_name = i
            ext = None
            flag = True
        object_logging(DirObject(obj_name, ext, flag, par_dir))


def parse_dir():
    parser = argparse.ArgumentParser(prog="Работа с директорией")
    parser.add_argument('-d', metavar='directory', default=os.getcwd())
    args = parser.parse_args()
    return tuple_gen(f'{args.d}')


if __name__ == '__main__':
    # request_dir()
    parse_dir()
