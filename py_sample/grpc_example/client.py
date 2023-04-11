import logging

import grpc
import helloworld_pb2
import helloworld_pb2_grpc


logging.basicConfig()


def main():
    port = "12345"
    print("Will try to greet world ...")
    with grpc.insecure_channel(f"localhost:{port}") as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name="you"))
    print(f"Greeter client received: {response.message}")


if __name__ == '__main__':
    main()
