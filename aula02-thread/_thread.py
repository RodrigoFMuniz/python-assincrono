import threading
import time


def alguma_coisa(param, a):
    print('Executa algo ...')
    print(f'Usa o parâmetro {param}---  {a}')

    return param * param


if __name__ == "__main__":
    print('\nIniciou antes da thread\n')
    time.sleep(2)
    th = threading.Thread(target=alguma_coisa, args=(42, 'olá',))
    print('\nIniciou antes da thread 2\n')
    time.sleep(200)
    th.start()
    print('\nIniciou antes do time\n')
    time.sleep(2)
    print('time')
    time.sleep(2)
    th.join()
    print('Finalizou após o time')
