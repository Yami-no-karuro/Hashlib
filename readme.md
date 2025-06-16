# Python wrapper for C hashing functions

## Introduction

[ctypes](https://docs.python.org/3/library/ctypes.html) is a foreign function library for **Python**.  
It provides **C** compatible data types, and allows calling functions in **DLLs** or **shared libraries**.  
It can be used to wrap these libraries in pure **Python**.

## The library itself

**LibHash** contains some of the most used hashing functions.

The **FNV-1a Hash** is a non-cryptographic hash function widely used for its simplicity, speed, and good distribution.  
It’s frequently used for hash tables, checksums, content identifiers, and more.

The **DJB2 Hash** function, created by Daniel J. Bernstein, is another popular non-cryptographic hash algorithm.  
It is known for its simplicity and effective distribution, commonly used in string hashing for hash tables and dictionaries.
