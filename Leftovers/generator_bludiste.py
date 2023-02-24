"""This module contains a function to generate a maze.
"""

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import networkx as nx
from typing import Tuple


def get_incidence(maze: np.ndarray) -> nx.DiGraph:
    """ Function to create an incidence graph from a maze.

    Args:
        maze (np.ndarray): nxn array of bools

    Returns:
        nx.DiGraph: incidence graph of the maze
    """
    (n_rows, n_cols) = maze.shape
    # incidence = np.zeros((n_rows * n_cols, n_rows * n_cols), dtype=int)
    # create a sparse matrix (lil_matrix) from the incidence matrix
    incidence = sp.sparse.lil_matrix((n_rows * n_cols, n_rows * n_cols))
    for i in range(n_rows):
        for j in range(n_cols):
            idx = i * n_cols + j
            if i > 0:
                incidence[idx, idx - n_cols] = 1
            if i < n_rows - 1:
                incidence[idx, idx + n_cols] = 1
            if j > 0:
                incidence[idx, idx - 1] = 1
            if j < n_cols - 1:
                incidence[idx, idx + 1] = 1
    cells = maze.copy().reshape(-1)
    incidence[cells, :] = 0
    incidence[:, cells] = 0
    # fill diagonal with 1
    incidence[np.diag_indices_from(incidence)] = 1
    graph_of_incidence = nx.DiGraph(incidence)
    return graph_of_incidence


def enhance_maze(maze, incidence_graph):
    """_summary_.

    Args:
        maze (_type_): _description_
        incidence_matrix (_type_): _description_

    Returns:
        _type_: _description_
    """
    (n_rows, n_cols) = maze.shape
    # find a random cell
    i = np.random.randint(n_rows)
    j = np.random.randint(n_cols)
    node_id = i * n_cols + j
    edges_remove = [(node_id, successor) for successor in
                    incidence_graph.successors(node_id)]
    incidence_graph.remove_edges_from(edges_remove)

    if nx.has_path(incidence_graph, 0, n_rows * n_cols - 1):
        maze[i, j] = True
        return maze, incidence_graph

    incidence_graph.add_edges_from(edges_remove)
    return maze, incidence_graph


def generate_maze(size_of_maze: int, n_iter: int = 100) -> \
        Tuple[np.ndarray, np.ndarray]:
    """Function to generate a maze.

    Args:
        size_of_maze (int): parameter to control the size of the maze
        n_iter (int, optional): how many times add an obstacle. Defaults to 100.

    Returns:
        Tuple[np.ndarray, np.ndarray]: _description_
    """

    # create a 2D bool array of size n x n
    # with all elements set to False
    maze_matrix = np.zeros((size_of_maze, size_of_maze), dtype=bool)
    maze_matrix[2:, 0] = True
    maze_matrix[:-1, -1] = True
    maze_matrix[0, 1:] = True
    maze_matrix[-1, :-2] = True
    maze_matrix[size_of_maze // 3, :-3] = True
    maze_matrix[(2 * size_of_maze) // 3, 2:] = True
    incidence_graph = get_incidence(maze_matrix)

    for _ in range(n_iter):
        maze_matrix, incidence_graph = enhance_maze(maze_matrix,
                                                    incidence_graph)

    return maze_matrix, incidence_graph


def main() -> None:
    """Test the function to generate a maze."""
    generated_maze, generated_graph = generate_maze(100, n_iter=8000)

    shortest_path = nx.shortest_path(generated_graph, 0, generated_maze.size - 1)
    # plot the maze in black and white and the shortest path in red
    # by creating an image with 3 channels
    generated_maze = np.repeat(1 - generated_maze[:, :, np.newaxis], 3, axis=2)
    for node in shortest_path:
        i, j = node // generated_maze.shape[1], node % generated_maze.shape[1]
        generated_maze[i, j, 0] = 1
        generated_maze[i, j, 1] = 0
        generated_maze[i, j, 2] = 0

    # convert into int8
    generated_maze = (generated_maze * 255).astype(np.uint8)
    print(generated_maze.shape)
    plt.imshow(generated_maze)
    plt.show()


if __name__ == '__main__':
    main()
