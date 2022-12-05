import threading
import time


def main():
    # threads = [
    #     threading.Thread(target=imprimir, args=('azul',)),
    #     threading.Thread(target=imprimir, args=('amarelo',)),
    #     threading.Thread(target=imprimir, args=('vermelho',)),
    #     threading.Thread(target=imprimir, args=('verde',))
    # ]
    th1 = threading.Thread(target=imprimir, args=('azul',))
    th2 = threading.Thread(target=imprimir, args=('amarelo',))
    th3 = threading.Thread(target=imprimir, args=('vermelho',))
    th4 = threading.Thread(target=imprimir, args=('verde',))

    th1.start()
    th1.join()
    th2.start()
    th2.join()
    th3.start()
    th3.join()
    th4.start()
    th4.join()

    # [th.start() for th in threads]
    # print('\nIniciando a thread\n')
    # [th.join() for th in threads]
    # print('\nFinalizando a thread\n')
    time.sleep(50)


def imprimir(cor):
    for i, c in enumerate(range(10)):
        print(f'Cor impressa: rodada {i} - {cor}\n')
        time.sleep(5)


if __name__ == "__main__":
    main()
