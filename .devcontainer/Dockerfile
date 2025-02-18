FROM python:3.13-slim

# Install ffmpeg
RUN apt-get update && apt-get install -y ffmpeg git gcc
RUN pip install --upgrade pip
RUN apt-get install -y dvipng texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended texlive-fonts-extra texlive-latex-recommended texlive-lang-european python3-pip git python3-mpi4py graphviz
RUN pip install --upgrade ipympl ipywidgets opencv-python jax jaxlib h5py ipykernel sympy pandas seaborn numpy matplotlib scipy sympy numba h5py line-profiler scalene numexpr ipykernel pandas seaborn pytest mypy cffi sphinx cython setuptools networkx graphviz
