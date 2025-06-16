from hashlib import fnv1a

filepath_a: str = "./source/file_a.txt"
with open(filepath_a, "rb") as f:
    content_a = f.read()

filepath_b: str = "./source/file_b.txt"
with open(filepath_b, "rb") as f:
    content_b = f.read()

hash_a = fnv1a(content_a)
hash_b = fnv1a(content_b)

print(f"Hash ({filepath_a}): {hash_a:#018x}")
print(f"Hash ({filepath_b}): {hash_b:#018x}")
