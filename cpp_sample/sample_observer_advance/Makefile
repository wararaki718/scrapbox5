CC=g++
CFLAGS=-std=c++11 -Wall -O2

all: main.o entity.o observer.o subject.o
	$(CC) $(CFLAGS) -o main main.o entity.o observer.o subject.o

main.o: main.cpp
	$(CC) $(CFLAGS) -o main.o -c main.cpp

entity.o: entity.cpp entity.hpp
	$(CC) $(CFLAGS) -o entity.o -c entity.cpp

observer.o: observer.cpp observer.hpp
	$(CC) $(CFLAGS) -o observer.o -c observer.cpp

subject.o: subject.cpp subject.hpp
	$(CC) $(CFLAGS) -o subject.o -c subject.cpp

clean:
	rm *.o main
