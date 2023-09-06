# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from SqlConnection.MySqlManager import Manager


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    manage = Manager("test")
    print(manage.read_one())
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
