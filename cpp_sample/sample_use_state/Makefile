CC=g++
CFLAGS=-std=c++11 -Wall -O2

all: main.o heroine.o
	$(CC) $(CFLAGS) -o main main.o heroine.o

main.o: main.cpp
	$(CC) $(CFLAGS) -o main.o -c main.cpp

heroine.o: heroine.cpp
	$(CC) $(CFLAGS) -o heroine.o -c heroine.cpp

clean:
	rm *.o main
