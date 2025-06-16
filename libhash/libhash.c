#include <stdint.h>
#include <string.h>

#include "libhash.h"

unsigned long fnv1a(const char *data, size_t len) 
{
    unsigned long hash = FNV_OFFSET_BASIS;
    for (size_t i = 0; i < len; i++) {
        hash ^= (uint8_t)data[i];
        hash *= FNV_PRIME;
    }

    return hash;
}

unsigned long djb2(const char *str) 
{
    unsigned long hash = DJB2_BASIS;
    int c;

    while ((c = (unsigned char)*str++))
        hash = ((hash << 5) + hash) + c; 

    return hash;
}
