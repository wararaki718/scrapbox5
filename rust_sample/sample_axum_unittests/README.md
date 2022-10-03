# axum unittest

## build

```shell
cargo build
```

## run

```shell
cargo run
```

check

```shell
curl localhost:3000
```

```shell
curl localhost:3000/ping
```

```shell
curl -H "Content-Type: application/json" -XPOST localhost:3000/sample -d "{\"name\": \"test\"}"
```

## test

```shell
cargo test
```
