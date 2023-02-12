CC=g++
CFLAGS=-std=c++11 -Wall -O2

all: main.o graph_node.o transform.o
	$(CC) $(CFLAGS) -o main main.o graph_node.o transform.o

main.o: main.cpp
	$(CC) $(CFLAGS) -o main.o -c main.cpp

graph_node.o: graph_node.cpp graph_node.hpp
	$(CC) $(CFLAGS) -o graph_node.o -c graph_node.cpp

transform.o: transform.cpp transform.hpp
	$(CC) $(CFLAGS) -o transform.o -c transform.cpp

clean:
	rm *.o main
