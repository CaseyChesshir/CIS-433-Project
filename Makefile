CXX = g++ -std=c++14 -Wall -g -Wno-write-strings

all: main

main: main.o
	$(CXX) website.cpp main.cpp -o main

run: 
	./main

clean:
	rm main.o main
