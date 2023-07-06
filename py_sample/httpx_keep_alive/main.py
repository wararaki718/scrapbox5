import httpx


def show(headers: httpx.Headers) -> None:
    for key, value in headers.items():
        print(f"  {key}: {value}")
    print()


def main() -> None:
    url = "http://localhost:80"
    limits = httpx.Limits(
        max_keepalive_connections=0,
        max_connections=None,
        keepalive_expiry=None
    )
    with httpx.Client() as client:
        response: httpx.Response = client.get(url)
        print(response.status_code)
        print("keep_alive=False:")
        show(response.headers)
    
    limits = httpx.Limits(max_keepalive_connections=5, max_connections=10)
    with httpx.Client(limits=limits) as client:
        response: httpx.Response = client.get(url)
        print(response.status_code)
        print("keep_alive=True:")
        show(response.headers)
    print("DONE")


if __name__ == "__main__":
    main()
