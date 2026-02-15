FROM python:3.14-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    dvipng \
    ffmpeg \
    git \
    graphviz \
    libopenmpi-dev \
    openmpi-bin \
    pkg-config \
    texlive-fonts-extra \
    texlive-fonts-recommended \
    texlive-lang-european \
    texlive-latex-extra \
    texlive-latex-recommended \
    && rm -rf /var/lib/apt/lists/*
