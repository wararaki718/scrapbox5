CC=g++
CFLAGS=-std=c++11 -Wall -O2

all: main.o ai_component.o physics_component.o game_entity.o render_component.o animation.o vector.o
	$(CC) $(CFLAGS) -o main main.o ai_component.o physics_component.o game_entity.o render_component.o animation.o vector.o

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

animation.o: animation.cpp animation.hpp
	$(CC) $(CFLAGS) -o animation.o -c animation.cpp

vector.o: vector.cpp vector.hpp
	$(CC) $(CFLAGS) -o vector.o -c vector.cpp

clean:
	rm *.o main
