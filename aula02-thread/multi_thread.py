import threading
import time


def main():
    threads = [
        threading.Thread(target=imprimir, args=('azul',)),
        threading.Thread(target=imprimir, args=('amarelo',)),
        threading.Thread(target=imprimir, args=('vermelho',)),
        threading.Thread(target=imprimir, args=('verde',))
    ]

    [th.start() for th in threads]
    print('\nIniciando a thread\n')
    [th.join() for th in threads]
    print('Finalizando a thread')


def imprimir(cor):
    for i, c in enumerate(range(10)):
        print(f'Cor impressa: rodada {i} - {cor}')
        time.sleep(1)


if __name__ == "__main__":
    main()
