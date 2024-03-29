import httpx


def show(headers: httpx.Headers) -> None:
    for key, value in headers.items():
        print(f"  {key}: {value}")
    print()


def main() -> None:
    url = "http://localhost:8080"

    print("# use client")
    print("[keep_alive=True]:")
    with httpx.Client() as client:
        response: httpx.Response = client.get(url)
        print(response.status_code)
        show(response.headers)
        request = client.build_request("GET", url)
        print(request.headers)
    print()

    print("[keep_alive=False]:")
    with httpx.Client(headers={"Connection": "close"}) as client:
        response: httpx.Response = client.get(url)
        print(response.status_code)
        show(response.headers)
        request = client.build_request("GET", url)
        print(request.headers)
    print()

    request = httpx.Request("GET", url)
    print(request.headers)

    print("DONE")


if __name__ == "__main__":
    main()
