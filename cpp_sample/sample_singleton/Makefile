CC=g++
CFLAGS=-std=c++11 -Wall -O2

all: main.o filesystem.o
	$(CC) $(CFLAGS) -o main main.o filesystem.o

main.o: main.cpp
	$(CC) $(CFLAGS) -o main.o -c main.cpp

filesystem.o: filesystem.cpp filesystem.hpp
	$(CC) $(CFLAGS) -o filesystem.o -c filesystem.cpp

clean:
	rm *.o main
