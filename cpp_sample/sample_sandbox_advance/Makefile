CC=g++
CFLAGS=-std=c++11 -Wall -O2

all: main.o particlesystem.o skylaunch.o superpower.o soundplayer.o
	$(CC) $(CFLAGS) -o main main.o particlesystem.o skylaunch.o superpower.o soundplayer.o

main.o: main.cpp
	$(CC) $(CFLAGS) -o main.o -c main.cpp

particlesystem.o: particlesystem.cpp particlesystem.hpp
	$(CC) $(CFLAGS) -o particlesystem.o -c particlesystem.cpp

skylaunch.o: skylaunch.cpp skylaunch.hpp
	$(CC) $(CFLAGS) -o skylaunch.o -c skylaunch.cpp

superpower.o: superpower.cpp superpower.hpp
	$(CC) $(CFLAGS) -o superpower.o -c superpower.cpp

soundplayer.o: soundplayer.cpp soundplayer.hpp
	$(CC) $(CFLAGS) -o soundplayer.o -c soundplayer.cpp

clean:
	rm *.o main
