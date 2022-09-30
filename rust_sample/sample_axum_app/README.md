# sample web app

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
curl -H "Content-Type: application/json" -XPOST localhost:3000/users -d "{\"username\": \"test\"}"
```
