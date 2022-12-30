CC=g++
CFLAGS=-std=c++11 -Wall -O2

all: main.o actor.o handler.o fire.o jump.o lurch.o swap.o
	$(CC) $(CFLAGS) -o main main.o actor.o handler.o fire.o jump.o lurch.o swap.o

main.o: main.cpp
	$(CC) $(CFLAGS) -o main.o -c main.cpp

actor.o: actor.cpp actor.hpp
	$(CC) $(CFLAGS) -o actor.o -c actor.cpp

handler.o: handler.cpp handler.hpp
	$(CC) $(CFLAGS) -o handler.o -c handler.cpp

fire.o: fire.cpp fire.hpp
	$(CC) $(CFLAGS) -o fire.o -c fire.cpp

jump.o: jump.cpp jump.hpp
	$(CC) $(CFLAGS) -o jump.o -c jump.cpp

lurch.o: lurch.cpp lurch.hpp
	$(CC) $(CFLAGS) -o lurch.o -c lurch.cpp

swap.o: swap.cpp swap.hpp
	$(CC) $(CFLAGS) -o swap.o -c swap.cpp

clean:
	rm *.o main
