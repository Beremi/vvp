#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

static void fill_with_sentinel(int32_t *buffer, size_t capacity) {
    for (size_t i = 0; i < capacity; ++i) {
        buffer[i] = -1;
    }
}

static int32_t find_max_vertex(const int32_t *edges, size_t n_edges) {
    int32_t max_vertex = edges[0];
    if (max_vertex < 0) {
        return -1;
    }

    for (size_t i = 1; i < n_edges; ++i) {
        if (edges[i] < 0) {
            return -1;
        }
        if (edges[i] > max_vertex) {
            max_vertex = edges[i];
        }
    }
    return max_vertex;
}

static int build_degree_index(
    const int32_t *edges,
    size_t m,
    size_t n_vertices,
    size_t *neighbor_index,
    size_t *neighbor_count) {
    for (size_t i = 0; i < 2 * m; ++i) {
        int32_t vertex = edges[i];
        if (vertex < 0 || (size_t)vertex >= n_vertices) {
            return 0;
        }
        neighbor_index[(size_t)vertex + 1] += 1;
    }

    for (size_t v = 0; v < n_vertices; ++v) {
        neighbor_count[v] = neighbor_index[v + 1];
    }

    for (size_t i = 1; i <= n_vertices; ++i) {
        neighbor_index[i] += neighbor_index[i - 1];
    }

    return 1;
}

static int build_neighbors(
    const int32_t *edges,
    size_t m,
    size_t n_vertices,
    int32_t *neighbors,
    const size_t *neighbor_index,
    int32_t **neighbor_lists) {
    size_t *tmp_index = (size_t *)malloc((n_vertices + 1) * sizeof(size_t));
    if (tmp_index == NULL) {
        return 0;
    }

    memcpy(tmp_index, neighbor_index, (n_vertices + 1) * sizeof(size_t));

    for (size_t i = 0; i < m; ++i) {
        int32_t u = edges[i];
        int32_t v = edges[i + m];

        neighbors[tmp_index[(size_t)u]++] = v;
        neighbors[tmp_index[(size_t)v]++] = u;
    }

    for (size_t v = 0; v < n_vertices; ++v) {
        neighbor_lists[v] = neighbors + neighbor_index[v];
    }

    free(tmp_index);
    return 1;
}

static size_t mask_to_indices(
    const bool *mask,
    size_t n_vertices,
    int32_t *indices,
    size_t capacity) {
    size_t count = 0;
    for (size_t i = 0; i < n_vertices; ++i) {
        if (mask[i]) {
            if (count < capacity) {
                indices[count] = (int32_t)i;
            }
            count += 1;
        }
    }

    size_t fill_start = count < capacity ? count : capacity;
    for (size_t i = fill_start; i < capacity; ++i) {
        indices[i] = -1;
    }

    return count;
}

size_t reachable_in_n_steps(
    const int32_t *edges,
    size_t m,
    size_t n_steps,
    int32_t *reachable_vertices,
    size_t reachable_capacity) {
    if (reachable_vertices == NULL || reachable_capacity == 0) {
        return 0;
    }
    fill_with_sentinel(reachable_vertices, reachable_capacity);

    if (m > 0 && edges == NULL) {
        return 0;
    }
    if (m > SIZE_MAX / 2) {
        return 0;
    }

    int32_t max_vertex = 0;
    if (m > 0) {
        max_vertex = find_max_vertex(edges, 2 * m);
        if (max_vertex < 0) {
            return 0;
        }
    }

    size_t n_vertices = (size_t)max_vertex + 1;
    size_t neighbors_capacity = m > 0 ? 2 * m : 1;

    size_t *neighbor_index = (size_t *)calloc(n_vertices + 1, sizeof(size_t));
    size_t *neighbor_count = (size_t *)calloc(n_vertices, sizeof(size_t));
    int32_t *neighbors = (int32_t *)calloc(neighbors_capacity, sizeof(int32_t));
    int32_t **neighbor_lists = (int32_t **)calloc(n_vertices, sizeof(int32_t *));
    bool *reachable = (bool *)calloc(n_vertices, sizeof(bool));
    bool *newly_reachable = (bool *)calloc(n_vertices, sizeof(bool));
    bool *next_reachable = (bool *)calloc(n_vertices, sizeof(bool));

    if (neighbor_index == NULL || neighbor_count == NULL || neighbors == NULL ||
        neighbor_lists == NULL || reachable == NULL ||
        newly_reachable == NULL || next_reachable == NULL) {
        free(neighbor_index);
        free(neighbor_count);
        free(neighbors);
        free(neighbor_lists);
        free(reachable);
        free(newly_reachable);
        free(next_reachable);
        return 0;
    }

    if (!build_degree_index(edges, m, n_vertices, neighbor_index, neighbor_count)) {
        free(neighbor_index);
        free(neighbor_count);
        free(neighbors);
        free(neighbor_lists);
        free(reachable);
        free(newly_reachable);
        free(next_reachable);
        return 0;
    }

    if (!build_neighbors(edges, m, n_vertices, neighbors, neighbor_index, neighbor_lists)) {
        free(neighbor_index);
        free(neighbor_count);
        free(neighbors);
        free(neighbor_lists);
        free(reachable);
        free(newly_reachable);
        free(next_reachable);
        return 0;
    }

    reachable[0] = true;
    newly_reachable[0] = true;

    for (size_t step = 0; step < n_steps; ++step) {
        memset(next_reachable, 0, n_vertices * sizeof(bool));

        for (size_t v = 0; v < n_vertices; ++v) {
            if (!newly_reachable[v]) {
                continue;
            }
            int32_t *adjacency = neighbor_lists[v];
            size_t degree = neighbor_count[v];
            for (size_t i = 0; i < degree; ++i) {
                next_reachable[(size_t)adjacency[i]] = true;
            }
        }

        bool any_new = false;
        for (size_t i = 0; i < n_vertices; ++i) {
            bool new_vertex = next_reachable[i] && !reachable[i];
            newly_reachable[i] = new_vertex;
            if (new_vertex) {
                any_new = true;
            }
            if (next_reachable[i]) {
                reachable[i] = true;
            }
        }

        if (!any_new) {
            break;
        }
    }

    size_t reachable_count = mask_to_indices(reachable, n_vertices, reachable_vertices, reachable_capacity);

    free(neighbor_index);
    free(neighbor_count);
    free(neighbors);
    free(neighbor_lists);
    free(reachable);
    free(newly_reachable);
    free(next_reachable);

    return reachable_count;
}
