FROM debian:testing AS build_stage

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python3 python3-pip  \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install pyyaml

COPY . .

RUN python3 main.py > index.html

FROM nginx
COPY --from=build_stage index.html /usr/share/nginx/html
