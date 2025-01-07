#include <iostream>
#include <vector>
using namespace std;

class Player {
    private:
        int id;
        int points;

    public:
        Player(int number);
        int getID();
        void setID(int newID);
        int getPoints();
        void setPoints(int newPoints);
};

class GyulHap {
    private:
        vector<vector<string>> board;
        vector<string> solutions;

        void createBoard();
        void printBoard();
        void findSolutions();

    public:
        GyulHap();
        vector<vector<string>> getBoard();
        vector<string> getSolutions();
        void playGame();
};

Player::Player(int number) {
    id = number;
    points = 0;
}

int Player::getID() {
    return this->id;
}

void Player::setID(int newID) {
    this->id = newID;
}

int Player::getPoints() {
    return this->points;
}

void Player::setPoints(int newPoints) {
    this->points = newPoints;
}

GyulHap::GyulHap() {
    createBoard();
    findSolutions();
}

void GyulHap::createBoard() {
    board = {{"123", "213", "111"}, {"231", "322", "333"}, {"132", "221", "313"}};
}

void GyulHap::printBoard() {
    for (int i = 0; i < board.size(); i++) {
        for (int j = 0; j < board[i].size(); j++) {
            cout << board[i][j] << " ";
        }
        cout << endl;
    }
}

void GyulHap::findSolutions() {

}

vector<vector<string>> GyulHap::getBoard() {
    return this->board;
}

vector<string> GyulHap::getSolutions() {
    return this->solutions;
}

void GyulHap::playGame() {
    printBoard();
}

int main() {
    GyulHap gameBoard;
    gameBoard.playGame();
    return 0;
}