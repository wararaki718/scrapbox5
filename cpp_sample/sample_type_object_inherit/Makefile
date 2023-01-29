CC=g++
CFLAGS=-std=c++11 -Wall -O2

all: main.o breed.o monster.o
	$(CC) $(CFLAGS) -o main main.o breed.o monster.o

main.o: main.cpp
	$(CC) $(CFLAGS) -o main.o -c main.cpp

breed.o: breed.cpp breed.hpp
	$(CC) $(CFLAGS) -o breed.o -c breed.cpp

monster.o: monster.cpp monster.hpp
	$(CC) $(CFLAGS) -o monster.o -c monster.cpp

clean:
	rm *.o main
