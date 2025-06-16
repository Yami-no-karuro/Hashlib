#ifndef LIBHASH_H
#define LIBHASH_H

#define FNV_OFFSET_BASIS 14695981039346656037ULL
#define FNV_PRIME 1099511628211U

#define DJB2_BASIS 5381

unsigned long fnv1a(const char *data, size_t len);
unsigned long djb2(const char *str);

#endif
