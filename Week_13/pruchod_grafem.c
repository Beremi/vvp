#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

int najdi_maximum(int *edges, int M)
{
    int max = edges[0];
    for (int i = 0; i < M; i++)
    {
        if (edges[i] > max)
            max = edges[i];
    }
    return max;
}

void spocti_sousedy_a_vyrob_index(int *edges, int M, int *edges_index_sousedu, int *pocet_sousedu, int n_vertices)
{
    for (int i = 0; i < M * 2; i++)
    {
        edges_index_sousedu[edges[i] + 1]++;
    }

    memcpy(pocet_sousedu, edges_index_sousedu + 1, n_vertices * sizeof(int));

    for (int i = 1; i <= n_vertices; i++)
    {
        edges_index_sousedu[i] += edges_index_sousedu[i - 1];
    }
}

void vyrob_edges_sousede(int *edges, int M, int *edges_sousede, int *edges_index_sousedu, int **sousedi_list_of_lists, int n_vertices)
{
    int *edges_tmp_index = (int *)calloc((n_vertices + 1), sizeof(int));
    memcpy(edges_tmp_index, edges_index_sousedu, (n_vertices + 1) * sizeof(int));

    for (int i = 0; i < M; i++)
    {
        edges_sousede[edges_tmp_index[edges[i]]++] = edges[i + M];
        edges_sousede[edges_tmp_index[edges[i + M]]++] = edges[i];
    }
    free(edges_tmp_index);

    for (int i = 0; i < n_vertices; i++)
    {
        sousedi_list_of_lists[i] = edges_sousede + edges_index_sousedu[i];
    }
}

void pridej_sousedy(bool *next_reachable, int *sousedi, int N)
{
    for (int i = 0; i < N; i++)
    {
        next_reachable[sousedi[i]] = true;
    }
}

void najdi_newly_reachable(bool *newly_reachable, bool *next_reachable, bool *reachable, int n_vertices)
{
    for (int i = 0; i < n_vertices; i++)
    {
        newly_reachable[i] = next_reachable[i] && !reachable[i];
    }
}

void updatuj_reachable(bool *reachable, bool *next_reachable, int n_vertices)
{
    for (int i = 0; i < n_vertices; i++)
    {
        reachable[i] = reachable[i] || next_reachable[i];
    }
}

bool pridali_jsme_neco(bool *newly_reachable, int n_vertices)
{
    for (int i = 0; i < n_vertices; i++)
    {
        if (newly_reachable[i])
            return true;
    }
    return false;
}

void prepis_masku_do_indexu(bool *mask, int *index, int n)
{
    int aktualni_pozice = 0;
    for (int i = 0; i < n; i++)
    {
        if (mask[i])
            index[aktualni_pozice++] = i;
    }
}

void reachable_in_n_steps(int *edges, int M, int n, int *reachable_vertices)
{
    int n_vertices = najdi_maximum(edges, M * 2) + 1;

    int *edges_index_sousedu = (int *)calloc(n_vertices + 1, sizeof(int));
    int *edges_sousede = (int *)calloc(2 * M, sizeof(int));

    int **sousedi_list_of_lists = (int **)calloc(n_vertices, sizeof(int *));
    int *pocet_sousedu = (int *)calloc(n_vertices, sizeof(int));

    bool *reachable = (bool *)calloc(n_vertices, sizeof(bool));
    bool *newly_reachable = (bool *)calloc(n_vertices, sizeof(bool));
    bool *next_reachable = (bool *)calloc(n_vertices, sizeof(bool));

    spocti_sousedy_a_vyrob_index(edges, M, edges_index_sousedu, pocet_sousedu, n_vertices);
    vyrob_edges_sousede(edges, M, edges_sousede, edges_index_sousedu, sousedi_list_of_lists, n_vertices);

    reachable[0] = true;
    newly_reachable[0] = true;

    for (int step = 0; step < n; step++)
    {
        memset(next_reachable, 0, n_vertices * sizeof(bool));
        for (int v = 0; v < n_vertices; v++)
        {
            if (newly_reachable[v])
            {
                pridej_sousedy(next_reachable, sousedi_list_of_lists[v], pocet_sousedu[v]);
            }
        }

        najdi_newly_reachable(newly_reachable, next_reachable, reachable, n_vertices);
        updatuj_reachable(reachable, next_reachable, n_vertices);

        if (!pridali_jsme_neco(newly_reachable, n_vertices))
            break;
    }

    prepis_masku_do_indexu(reachable, reachable_vertices, n_vertices);

    free(edges_index_sousedu);
    free(edges_sousede);
    free(newly_reachable);
    free(next_reachable);
    free(sousedi_list_of_lists);
    free(pocet_sousedu);
    free(reachable);
}
