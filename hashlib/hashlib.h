#ifndef LIBHASH_H
#define LIBHASH_H

#define FNV_OFFSET_BASIS 14695981039346656037ULL
#define FNV_PRIME 1099511628211U

unsigned long fnv1a(const char *data, size_t len);

#endif
