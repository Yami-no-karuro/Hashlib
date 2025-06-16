from libhash.bindings import fnv1a
from libhash.bindings import djb2

filepath_a: str = "./source/file_a.txt"
with open(filepath_a, "rb") as f:
    content_a = f.read()

filepath_b: str = "./source/file_b.txt"
with open(filepath_b, "rb") as f:
    content_b = f.read()

fnv1a_a = fnv1a(content_a)
fnv1a_b = fnv1a(content_b)

djb2_a = djb2(content_a)
djb2_b = djb2(content_b)

print(f"FNV1a digest ({filepath_a}): {fnv1a_a:#018x}")
print(f"DJB2 digest ({filepath_a}): {fnv1a_b:#018x}")
print(f"FNV1a digest ({filepath_b}): {djb2_a:#018x}")
print(f"DJB2 digest ({filepath_b}): {djb2_b:#018x}")
