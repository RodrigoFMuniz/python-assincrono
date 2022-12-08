import threading
import typing
import random
import time


class Conta:
    def __init__(self, saldo=0) -> None:
        self.saldo = saldo


if __name__ == "__main__":
    contas = criar_contas()
    total = sum(conta.saldo for conta in contas)
    print('Iniciando transferências...')
