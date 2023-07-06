import httpx


def show(headers: httpx.Headers) -> None:
    for key, value in headers.items():
        print(f"  {key}: {value}")
    print()


def main() -> None:
    url = "http://localhost:8080"
    with httpx.Client(headers={"Connection": "close"}) as client:
        response: httpx.Response = client.get(url)
        print(response.status_code)
        print("keep_alive=False:")
        show(response.headers)
    
    with httpx.Client() as client:
        response: httpx.Response = client.get(url)
        print(response.status_code)
        print("keep_alive=True:")
        show(response.headers)
    print("DONE")


if __name__ == "__main__":
    main()
