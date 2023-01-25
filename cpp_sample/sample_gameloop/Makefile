CC=g++
CFLAGS=-std=c++11 -Wall -O2

all: main.o
	$(CC) $(CFLAGS) -o main main.o

main.o: main.cpp
	$(CC) $(CFLAGS) -o main.o -c main.cpp

clean:
	rm *.o main
