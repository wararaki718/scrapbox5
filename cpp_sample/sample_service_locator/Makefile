CC=g++
CFLAGS=-std=c++11 -Wall -O2

all: main.o console_audio.o locator.o null_audio.o
	$(CC) $(CFLAGS) -o main main.o console_audio.o locator.o null_audio.o

main.o: main.cpp
	$(CC) $(CFLAGS) -o main.o -c main.cpp

console_audio.o: console_audio.cpp console_audio.hpp
	$(CC) $(CFLAGS) -o console_audio.o -c console_audio.cpp

locator.o: locator.cpp locator.hpp
	$(CC) $(CFLAGS) -o locator.o -c locator.cpp

null_audio.o: null_audio.cpp null_audio.hpp
	$(CC) $(CFLAGS) -o null_audio.o -c null_audio.cpp

clean:
	rm *.o main
