import threading
import time


def alguma_coisa(param):
    print('Executa algo ...')
    print(f'Usa o parâmetro {param}')

    return param * param


th = threading.Thread(target=alguma_coisa, args=(42,))
th.start()
th.join()
time.sleep(2)
print('Finalizou após o time')
