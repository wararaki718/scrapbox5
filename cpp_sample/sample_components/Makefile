CC=g++
CFLAGS=-std=c++11 -Wall -O2

all: main.o bjorn.o graphics.o world.o graphics_component.o input_component.o physics_component.o
	$(CC) $(CFLAGS) -o main main.o bjorn.o graphics.o world.o graphics_component.o input_component.o physics_component.o

main.o: main.cpp
	$(CC) $(CFLAGS) -o main.o -c main.cpp

bjorn.o: bjorn.cpp bjorn.hpp
	$(CC) $(CFLAGS) -o bjorn.o -c bjorn.cpp

graphics.o: graphics.cpp graphics.hpp
	$(CC) $(CFLAGS) -o graphics.o -c graphics.cpp

world.o: world.cpp world.hpp
	$(CC) $(CFLAGS) -o world.o -c world.cpp

graphics_component.o: graphics_component.cpp graphics_component.hpp
	$(CC) $(CFLAGS) -o graphics_component.o -c graphics_component.cpp

input_component.o: input_component.cpp input_component.hpp
	$(CC) $(CFLAGS) -o input_component.o -c input_component.cpp

physics_component.o: physics_component.cpp physics_component.hpp
	$(CC) $(CFLAGS) -o physics_component.o -c physics_component.cpp

clean:
	rm *.o main
