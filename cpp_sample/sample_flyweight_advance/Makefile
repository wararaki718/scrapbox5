CC=g++
CFLAGS=-std=c++11 -Wall -O2

all: main.o terrain.o world.o
	$(CC) $(CFLAGS) -o main main.o terrain.o world.o

main.o: main.cpp
	$(CC) $(CFLAGS) -o main.o -c main.cpp

terrain.o: terrain.cpp terrain.hpp
	$(CC) $(CFLAGS) -o terrain.o -c terrain.cpp

world.o: world.cpp world.hpp
	$(CC) $(CFLAGS) -o world.o -c world.cpp

clean:
	rm *.o main
