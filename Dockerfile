FROM continuumio/conda-concourse-ci
RUN git clone https://github.com/brittainhard/conda_recipes.git
RUN yum install vim -y
RUN cd conda_recipes
