CC=g++
CFLAGS=-std=c++11 -Wall -O2

all: main.o audio.o menu.o
	$(CC) $(CFLAGS) -o main main.o audio.o menu.o

main.o: main.cpp
	$(CC) $(CFLAGS) -o main.o -c main.cpp

audio.o: audio.cpp audio.hpp
	$(CC) $(CFLAGS) -o audio.o -c audio.cpp

menu.o: menu.cpp menu.hpp
	$(CC) $(CFLAGS) -o menu.o -c menu.cpp

clean:
	rm *.o main
