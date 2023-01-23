CC=g++
CFLAGS=-std=c++11 -Wall -O2

all: main.o actor.o comedian.o stage.o
	$(CC) $(CFLAGS) -o main main.o actor.o comedian.o stage.o

main.o: main.cpp
	$(CC) $(CFLAGS) -o main.o -c main.cpp

actor.o: actor.cpp actor.hpp
	$(CC) $(CFLAGS) -o actor.o -c actor.cpp

comedian.o: comedian.cpp comedian.hpp
	$(CC) $(CFLAGS) -o comedian.o -c comedian.cpp

stage.o: stage.cpp stage.hpp
	$(CC) $(CFLAGS) -o stage.o -c stage.cpp

clean:
	rm *.o main
