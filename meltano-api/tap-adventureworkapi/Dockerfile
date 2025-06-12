ARG MELTANO_IMAGE=meltano/meltano:latest-python3.11
FROM $MELTANO_IMAGE


RUN apt update && \
    apt install -y curl && \
    apt install -y unzip

RUN curl -fsSL https://raw.githubusercontent.com/databricks/setup-cli/main/install.sh | sh

WORKDIR /projects/meltano-api

COPY . .

RUN pip install -e .

RUN meltano lock --update --all && \
    meltano install

#ENTRYPOINT [ "/bin/bash", "-c"]
ENTRYPOINT [ "./entrypoint.sh"]