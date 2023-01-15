CC=g++
CFLAGS=-std=c++11 -Wall -O2

all: main.o demon.o ghost.o sorcerer.o
	$(CC) $(CFLAGS) -o main main.o demon.o ghost.o sorcerer.o

main.o: main.cpp
	$(CC) $(CFLAGS) -o main.o -c main.cpp

demon.o: demon.cpp demon.hpp
	$(CC) $(CFLAGS) -o demon.o -c demon.cpp

ghost.o: ghost.cpp ghost.hpp
	$(CC) $(CFLAGS) -o ghost.o -c ghost.cpp

sorcerer.o: sorcerer.cpp sorcerer.hpp
	$(CC) $(CFLAGS) -o sorcerer.o -c sorcerer.cpp

clean:
	rm *.o main
