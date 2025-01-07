#include <iostream>
#include <vector>
using namespace std;

class Player {
    // id / index / name?
    // Points
    private:
        int id;
        int points;
    public:
        Player();
};

class GyulHap {
    //Private
        //Board
        //Array of Solutions

        //Print Board
        //Make Board
        //Find Solutions
    private:
        vector<vector<string>> board;
        vector<string> solutions;

        void createBoard();
        void printBoard();
        void findSolutions();
    
    //Public
        // Initialize Board?
            // - Make board
            // - find solutions
        // Play Game
            // - Print board at beginning
            // - Alternate turns
            // - Players guess a solution
            // - gives points accordingly
    public:
        GyulHap(); //Make Board, Make Array of solutions (Call Functions)
        void playGame();
};

void GyulHap::createBoard() {

}

void GyulHap::printBoard() {

}

void GyulHap::findSolutions() {

}

GyulHap::GyulHap() {

}

void GyulHap::playGame() {

}

int main() {
    // Choose number of players and number of rounds
    // cout << "Hello World" << endl;
    // Player player1;
    GyulHap game1;
    return 0;
}