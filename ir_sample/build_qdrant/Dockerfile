FROM amazonlinux:2 as chef

RUN yum update -y
# RUN amazon-linux-extras install -y rust1
RUN (yum install -y gcc-multilib || echo "Warning: not installing gcc-multilib" )
RUN yum install -y gcc gcc-c++ cmake protobuf-compiler gcc-aarch64-linux-gnu g++-aarch64-linux-gnu curl libssl-dev git
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- --default-toolchain stable -y
ENV PATH="/root/.cargo/bin:${PATH}"
RUN cargo install cargo-chef --locked

RUN git clone https://github.com/qdrant/qdrant.git -b v1.1.0 --depth 1
WORKDIR /qdrant


FROM chef AS planner
RUN cargo chef prepare --recipe-path recipe.json


FROM chef as builder
# based on https://github.com/docker/buildx/issues/510
ARG TARGETARCH
ENV TARGETARCH=${TARGETARCH:-amd64}

WORKDIR /qdrant
RUN mv ./tools/target_arch.sh ./target_arch.sh
RUN echo "Building for $TARGETARCH, arch: $(bash target_arch.sh)"

COPY --from=planner /qdrant/recipe.json recipe.json

RUN rustup component add rustfmt
RUN rustup target add $(bash target_arch.sh)

# Build dependencies - this is the caching Docker layer!
RUN cargo chef cook --release --target $(bash target_arch.sh) --recipe-path recipe.json

# Build actual target here
RUN cargo build --release --target $(bash target_arch.sh) --bin qdrant
RUN mv target/$(bash target_arch.sh)/release/qdrant /qdrant/qdrant


FROM amazonlinux:2
ARG APP=/qdrant

RUN yum update -y \
    && yum install -y ca-certificates tzdata

EXPOSE 6333
EXPOSE 6334

ENV TZ=Etc/UTC \
    RUN_MODE=production

RUN mkdir -p ${APP}

COPY --from=builder /qdrant/qdrant ${APP}/qdrant
COPY --from=builder /qdrant/config ${APP}/config

WORKDIR ${APP}

CMD ["./qdrant"]
