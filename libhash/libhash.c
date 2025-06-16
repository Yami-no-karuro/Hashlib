#include <stdint.h>
#include <string.h>

#include "libhash.h"

unsigned long fnv1a(const char *data, size_t len) {
    unsigned long hash = FNV_OFFSET_BASIS;
    for (size_t i = 0; i < len; i++) {
        hash ^= (uint8_t)data[i];
        hash *= FNV_PRIME;
    }

    return hash;
}
