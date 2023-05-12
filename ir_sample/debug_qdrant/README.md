# debug qdrant

## setup

```shell
brew install protobuf
```

```shell
rustup upgrade
```

```shell
brew tap messense/macos-cross-toolchains
brew install aarch64-unknown-linux-gnu
```

```shell
rustup target add aarch64-unknown-linux-gnu
```

## download

```shell
git clone https://github.com/qdrant/qdrant.git
```

## build

```shell
cd qdrant
cargo build --target aarch64-unknown-linux-gnu --bin qdrant
```

```shell
cargo build --release --target aarch64-unknown-linux-gnu --bin qdrant
```

## run

```shell
cd qdrant
cp target/debug/qdrant .
./qdrant
```
