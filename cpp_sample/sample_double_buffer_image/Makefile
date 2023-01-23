CC=g++
CFLAGS=-std=c++11 -Wall -O2

all: main.o buffer.o scene.o
	$(CC) $(CFLAGS) -o main main.o buffer.o scene.o

main.o: main.cpp
	$(CC) $(CFLAGS) -o main.o -c main.cpp

buffer.o: buffer.cpp buffer.hpp
	$(CC) $(CFLAGS) -o buffer.o -c buffer.cpp

scene.o: scene.cpp scene.hpp
	$(CC) $(CFLAGS) -o scene.o -c scene.cpp

clean:
	rm *.o main
