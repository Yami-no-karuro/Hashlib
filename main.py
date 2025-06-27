from libhash.bindings import fnv1a
from libhash.bindings import fnv1a_file
from libhash.bindings import djb2

input: bytes = b"Hello, my name is Yami-no-karuro and i'm a software developer."
file_a: str = "source/file_a.txt"
file_b: str = "source/file_b.txt"

fnv1a_digest: int = fnv1a(input)
print(f"FNV-1a digest: {fnv1a_digest:#018x}")

djb2_digest: int = djb2(input)
print(f"DJB2 digest: {djb2_digest:#018x}")

file_a_digest: int = fnv1a_file(file_a)
file_b_digest: int = fnv1a_file(file_b)
if (file_a_digest == file_b_digest):
    print(f"No difference found between \"{file_a}\" and \"{file_b}\".")
    print("The files are equals.")
