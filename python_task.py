import datetime


def current_time(msg):
    print(f'{datetime.datetime.now()} - {msg}')


def main():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            current_time("Niv8200")
        elif i % 3 == 0:
            current_time("Niv")
        elif i % 5 == 0:
            current_time("8200")
        else:
            print(i)


if __name__ == '__main__':
    main()
