CC=g++
CFLAGS=-std=c++11 -Wall -O2

all: main.o achievements.o entity.o physics.o subject.o
	$(CC) $(CFLAGS) -o main main.o achievements.o entity.o physics.o subject.o

main.o: main.cpp
	$(CC) $(CFLAGS) -o main.o -c main.cpp

achievements.o: achievements.cpp achievements.hpp
	$(CC) $(CFLAGS) -o achievements.o -c achievements.cpp

entity.o: entity.cpp entity.hpp
	$(CC) $(CFLAGS) -o entity.o -c entity.cpp

physics.o: physics.cpp physics.hpp
	$(CC) $(CFLAGS) -o physics.o -c physics.cpp

subject.o: subject.cpp subject.hpp
	$(CC) $(CFLAGS) -o subject.o -c subject.cpp

clean:
	rm *.o main
