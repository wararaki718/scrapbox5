CC=g++
CFLAGS=-std=c++11 -Wall -O2

all: main.o game_object.o graphics.o world.o bjorn_graphics_component.o player_input_component.o bjorn_physics_component.o
	$(CC) $(CFLAGS) -o main main.o game_object.o graphics.o world.o bjorn_graphics_component.o player_input_component.o bjorn_physics_component.o

main.o: main.cpp
	$(CC) $(CFLAGS) -o main.o -c main.cpp

game_object.o: game_object.cpp game_object.hpp
	$(CC) $(CFLAGS) -o game_object.o -c game_object.cpp

graphics.o: graphics.cpp graphics.hpp
	$(CC) $(CFLAGS) -o graphics.o -c graphics.cpp

world.o: world.cpp world.hpp
	$(CC) $(CFLAGS) -o world.o -c world.cpp

bjorn_graphics_component.o: bjorn_graphics_component.cpp bjorn_graphics_component.hpp
	$(CC) $(CFLAGS) -o bjorn_graphics_component.o -c bjorn_graphics_component.cpp

player_input_component.o: player_input_component.cpp player_input_component.hpp
	$(CC) $(CFLAGS) -o player_input_component.o -c player_input_component.cpp

bjorn_physics_component.o: bjorn_physics_component.cpp bjorn_physics_component.hpp
	$(CC) $(CFLAGS) -o bjorn_physics_component.o -c bjorn_physics_component.cpp

clean:
	rm *.o main
