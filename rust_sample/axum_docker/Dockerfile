FROM rust:1.64.0 as builder
ARG PROJECT_NAME=axum_docker

RUN USER=root cargo new --bin ${PROJECT_NAME}
WORKDIR /${PROJECT_NAME}

# build empty app with downloaded dependencies to produce a stable image layer
COPY Cargo.lock Cargo.lock
COPY Cargo.toml Cargo.toml
RUN cargo build --release
RUN rm ./target/release/deps/${PROJECT_NAME}*

# build web app
RUN rm src/*.rs
COPY src src
RUN cargo build --release

FROM debian:buster-slim
ARG PROJECT_NAME=axum_docker
COPY --from=builder /${PROJECT_NAME}/target/release/${PROJECT_NAME} ./app

CMD ["./app"]