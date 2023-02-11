CC=g++
CFLAGS=-std=c++11 -Wall -O2

all: main.o particle.o particle_system.o
	$(CC) $(CFLAGS) -o main main.o particle.o particle_system.o

main.o: main.cpp
	$(CC) $(CFLAGS) -o main.o -c main.cpp

particle.o: particle.cpp particle.hpp
	$(CC) $(CFLAGS) -o particle.o -c particle.cpp

particle_system.o: particle_system.cpp particle_system.hpp
	$(CC) $(CFLAGS) -o particle_system.o -c particle_system.cpp

clean:
	rm *.o main
