CC=g++
CFLAGS=-std=c++11 -Wall -O2

all: main.o entity.o skeleton.o statue.o world.o
	$(CC) $(CFLAGS) -o main main.o entity.o skeleton.o statue.o world.o

main.o: main.cpp
	$(CC) $(CFLAGS) -o main.o -c main.cpp

entity.o: entity.cpp entity.hpp
	$(CC) $(CFLAGS) -o entity.o -c entity.cpp

skeleton.o: skeleton.cpp skeleton.hpp
	$(CC) $(CFLAGS) -o skeleton.o -c skeleton.cpp

statue.o: statue.cpp statue.hpp
	$(CC) $(CFLAGS) -o statue.o -c statue.cpp

world.o: world.cpp world.hpp
	$(CC) $(CFLAGS) -o world.o -c world.cpp

clean:
	rm *.o main
