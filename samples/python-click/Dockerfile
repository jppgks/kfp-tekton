FROM continuumio/miniconda3

RUN echo "source activate base" > ~/.bashrc
ENV PATH /opt/conda/envs/base/bin:$PATH
RUN conda install click

COPY print_arg.py .
