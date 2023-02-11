CC=g++
CFLAGS=-std=c++11 -Wall -O2

all: main.o ai_component.o physics_component.o game_entity.o render_component.o particle.o particle_system.o
	$(CC) $(CFLAGS) -o main main.o ai_component.o physics_component.o game_entity.o render_component.o particle.o particle_system.o

main.o: main.cpp
	$(CC) $(CFLAGS) -o main.o -c main.cpp

ai_component.o: ai_component.cpp ai_component.hpp
	$(CC) $(CFLAGS) -o ai_component.o -c ai_component.cpp

physics_component.o: physics_component.cpp physics_component.hpp
	$(CC) $(CFLAGS) -o physics_component.o -c physics_component.cpp

render_component.o: render_component.cpp render_component.hpp
	$(CC) $(CFLAGS) -o render_component.o -c render_component.cpp

game_entity.o: game_entity.cpp game_entity.hpp
	$(CC) $(CFLAGS) -o game_entity.o -c game_entity.cpp

particle.o: particle.cpp particle.hpp
	$(CC) $(CFLAGS) -o particle.o -c particle.cpp

particle_system.o: particle_system.cpp particle_system.hpp
	$(CC) $(CFLAGS) -o particle_system.o -c particle_system.cpp

clean:
	rm *.o main
