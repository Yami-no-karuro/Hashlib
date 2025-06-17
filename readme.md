# Python wrapper for LibHash (C)

## Introduction

The project is based on [ctypes](https://docs.python.org/3/library/ctypes.html), a foreign function library for **Python**.  
It provides **C** compatible data types, and allows calling functions in **DLLs** or **shared libraries**.

## LibHash

**LibHash** contains some of the most used hashing functions.

The **FNV-1a Hash** is a **non-cryptographic** hash function widely used for its simplicity, speed, and good distribution.  
It’s frequently used for hash tables, checksums, content identifiers, and more.

The **DJB2 Hash** function, created by **Daniel J. Bernstein**, is another popular **non-cryptographic** hash algorithm.  
It is known for its simplicity and effective distribution, commonly used in string hashing for hash tables and dictionaries.  
(More on [FNV-1a](https://en.wikipedia.org/wiki/Fowler%E2%80%93Noll%E2%80%93Vo_hash_function) and [Hash functions](https://en.wikipedia.org/wiki/Hash_function) on [Wikipedia](https://en.wikipedia.org))
