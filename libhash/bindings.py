import ctypes
import os

libpath: str = os.path.abspath("libhash/build/libhash.so")
lib = ctypes.CDLL(libpath)

lib.fnv1a.argtypes = [ctypes.c_char_p, ctypes.c_size_t]
lib.fnv1a.restype = ctypes.c_uint64

def fnv1a(data: bytes) -> int:
    return lib.fnv1a(data, len(data))
