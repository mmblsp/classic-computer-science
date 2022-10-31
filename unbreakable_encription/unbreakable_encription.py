from typing import Tuple
from secrets import token_bytes


def random_key(length: int) -> int:
    """generate token key"""
    tbk: bytes = token_bytes(length)
    return int.from_bytes(tbk, "big")


def encrypt(original: str) -> Tuple[int, int]:
    """encrypt"""
    original_bytes: bytes = original.encode()
    dummy: int = random_key(len(original_bytes))
    original_key: int = int.from_bytes(original_bytes, "big")
    encrypted: int = original_key ^ dummy
    return dummy, encrypted


def decrypt(key_one: int, key_nxt: int) -> str:
    """decript"""
    decripted: int = key_one ^ key_nxt
    temp: bytes = decripted.to_bytes((decripted.bit_length()+7) // 8, "big")
    return temp.decode()


if __name__ == "__main__":
    key1, key2 = encrypt("One Time Pad!")
    result: str = decrypt(key1, key2)
    print(result)
