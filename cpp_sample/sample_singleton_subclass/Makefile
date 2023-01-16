CC=g++
CFLAGS=-std=c++11 -Wall -O2

all: main.o filesystem.o ps3.o wii.o
	$(CC) $(CFLAGS) -o main main.o filesystem.o ps3.o wii.o

main.o: main.cpp
	$(CC) $(CFLAGS) -o main.o -c main.cpp

filesystem.o: filesystem.cpp filesystem.hpp
	$(CC) $(CFLAGS) -o filesystem.o -c filesystem.cpp

ps3.o: ps3.cpp ps3.hpp
	$(CC) $(CFLAGS) -o ps3.o -c ps3.cpp

wii.o: wii.cpp wii.hpp
	$(CC) $(CFLAGS) -o wii.o -c wii.cpp

clean:
	rm *.o main
