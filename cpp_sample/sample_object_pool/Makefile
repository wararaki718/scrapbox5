CC=g++
CFLAGS=-std=c++11 -Wall -O2

all: main.o particle.o particle_pool.o
	$(CC) $(CFLAGS) -o main main.o particle.o particle_pool.o

main.o: main.cpp
	$(CC) $(CFLAGS) -o main.o -c main.cpp

particle.o: particle.cpp particle.hpp
	$(CC) $(CFLAGS) -o particle.o -c particle.cpp

particle_pool.o: particle_pool.cpp particle_pool.hpp
	$(CC) $(CFLAGS) -o particle_pool.o -c particle_pool.cpp

clean:
	rm *.o main
