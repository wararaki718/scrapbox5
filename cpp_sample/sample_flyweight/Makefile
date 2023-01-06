CC=g++
CFLAGS=-std=c++11 -Wall -O2

all: main.o tree.o
	$(CC) $(CFLAGS) -o main main.o tree.o

main.o: main.cpp
	$(CC) $(CFLAGS) -o main.o -c main.cpp

tree.o: tree.cpp tree.hpp
	$(CC) $(CFLAGS) -o tree.o -c tree.cpp

clean:
	rm *.o main
