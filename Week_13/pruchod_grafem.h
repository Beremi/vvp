#ifndef PRUCHOD_GRAFEM_H
#define PRUCHOD_GRAFEM_H

#include <stddef.h>
#include <stdint.h>

size_t reachable_in_n_steps(
    const int32_t *edges,
    size_t m,
    size_t n_steps,
    int32_t *reachable_vertices,
    size_t reachable_capacity
);

#endif
