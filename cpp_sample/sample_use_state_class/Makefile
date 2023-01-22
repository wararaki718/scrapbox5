CC=g++
CFLAGS=-std=c++11 -Wall -O2

all: main.o heroine.o heroine_state.o diving_state.o ducking_state.o jumping_state.o standing_state.o
	$(CC) $(CFLAGS) -o main main.o heroine.o heroine_state.o diving_state.o ducking_state.o jumping_state.o standing_state.o

main.o: main.cpp
	$(CC) $(CFLAGS) -o main.o -c main.cpp

heroine.o: heroine.cpp heroine.hpp
	$(CC) $(CFLAGS) -o heroine.o -c heroine.cpp

heroine_state.o: heroine_state.cpp heroine_state.hpp
	$(CC) $(CFLAGS) -o heroine_state.o -c heroine_state.cpp

diving_state.o: diving_state.cpp diving_state.hpp
	$(CC) $(CFLAGS) -o diving_state.o -c diving_state.cpp

ducking_state.o: ducking_state.cpp ducking_state.hpp
	$(CC) $(CFLAGS) -o ducking_state.o -c ducking_state.cpp

jumping_state.o: jumping_state.cpp jumping_state.hpp
	$(CC) $(CFLAGS) -o jumping_state.o -c jumping_state.cpp

standing_state.o: standing_state.cpp standing_state.hpp
	$(CC) $(CFLAGS) -o standing_state.o -c standing_state.cpp

clean:
	rm *.o main
