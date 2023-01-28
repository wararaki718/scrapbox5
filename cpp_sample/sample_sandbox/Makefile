CC=g++
CFLAGS=-std=c++11 -Wall -O2

all: main.o skylaunch.o superpower.o
	$(CC) $(CFLAGS) -o main main.o skylaunch.o superpower.o

main.o: main.cpp
	$(CC) $(CFLAGS) -o main.o -c main.cpp

skylaunch.o: skylaunch.cpp skylaunch.hpp
	$(CC) $(CFLAGS) -o skylaunch.o -c skylaunch.cpp

superpower.o: superpower.cpp superpower.hpp
	$(CC) $(CFLAGS) -o superpower.o -c superpower.cpp

clean:
	rm *.o main
