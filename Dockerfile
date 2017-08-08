FROM continuumio/conda-concourse-ci
ADD . conda_recipes
RUN yum install vim -y
