CXX = g++ -std=c++14 -Wall -g -Wno-write-strings

all: main

main: main.o
	$(CXX) main.cpp -o main

run: 
	./main

clean:
	rm main.o main
