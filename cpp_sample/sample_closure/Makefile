CC=g++
CFLAGS=-std=c++11 -Wall -O2

all: main.o move.o handler.o unit.o
	$(CC) $(CFLAGS) -o main main.o move.o handler.o unit.o

main.o: main.cpp
	$(CC) $(CFLAGS) -o main.o -c main.cpp

move.o: move.cpp move.hpp
	$(CC) $(CFLAGS) -o move.o -c move.cpp

handler.o: handler.cpp handler.hpp
	$(CC) $(CFLAGS) -o handler.o -c handler.cpp

unit.o: unit.cpp unit.hpp
	$(CC) $(CFLAGS) -o unit.o -c unit.cpp

clean:
	rm *.o main
