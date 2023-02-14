CC=g++
CFLAGS=-std=c++11 -Wall -O2

all: main.o grid.o unit.o
	$(CC) $(CFLAGS) -o main main.o grid.o unit.o

main.o: main.cpp
	$(CC) $(CFLAGS) -o main.o -c main.cpp

grid.o: grid.cpp grid.hpp
	$(CC) $(CFLAGS) -o grid.o -c grid.cpp

unit.o: unit.cpp unit.hpp
	$(CC) $(CFLAGS) -o unit.o -c unit.cpp

clean:
	rm *.o main
