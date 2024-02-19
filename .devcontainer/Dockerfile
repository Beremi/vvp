FROM python:3.11-slim

# Install ffmpeg
RUN apt-get update && apt-get install -y ffmpeg git gcc
RUN pip install --upgrade pip
RUN apt-get install python3-pip python3-numpy python3-matplotlib python3-scipy python3-sympy python3-numba cython3 python3-mpi4py python3-h5py git python3-line-profiler python3-scalene python3-numexpr python3-ipykernel python3-pandas python3-seaborn python3-pytest python3-mypy python3-cffi
