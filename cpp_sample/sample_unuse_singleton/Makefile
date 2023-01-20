CC=g++
CFLAGS=-std=c++11 -Wall -O2

all: main.o enemy.o log.o object.o
	$(CC) $(CFLAGS) -o main main.o enemy.o log.o object.o

main.o: main.cpp
	$(CC) $(CFLAGS) -o main.o -c main.cpp

enemy.o: enemy.cpp enemy.hpp
	$(CC) $(CFLAGS) -o enemy.o -c enemy.cpp

log.o: log.cpp log.hpp
	$(CC) $(CFLAGS) -o log.o -c log.cpp

object.o: object.cpp object.hpp
	$(CC) $(CFLAGS) -o object.o -c object.cpp

clean:
	rm *.o main
