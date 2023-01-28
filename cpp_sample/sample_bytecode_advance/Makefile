CC=g++
CFLAGS=-std=c++11 -Wall -O2

all: main.o command.o vm.o
	$(CC) $(CFLAGS) -o main main.o command.o vm.o

main.o: main.cpp
	$(CC) $(CFLAGS) -o main.o -c main.cpp

command.o: command.cpp command.hpp
	$(CC) $(CFLAGS) -o command.o -c command.cpp

vm.o: vm.cpp
	$(CC) $(CFLAGS) -o vm.o -c vm.cpp

clean:
	rm *.o main
