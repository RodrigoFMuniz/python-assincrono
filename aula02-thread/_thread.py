import threading
import time


def alguma_coisa(param, a):
    print('Executa algo ...')
    print(f'Usa o parâmetro {param}---  {a}')

    return param * param


if __name__ == "__main__":
    th = threading.Thread(target=alguma_coisa, args=(42, 'olá',))
    th.start()
    th.join()
    time.sleep(2)
    print('Finalizou após o time')
