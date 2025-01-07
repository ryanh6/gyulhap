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

}

void GyulHap::createBoard() {

}

void GyulHap::printBoard() {
    // cout << endl;
    //     for (const auto &row : board) {
    //         for (const auto &cell : row) {
    //             cout << cell << " ";
    //         }
    //         cout << endl;
    //     }
    // cout << endl;
}

void GyulHap::findSolutions() {

}

// vector<vector<string>> GyulHap::getBoard() {
//     return;
// }

// vector<string> GyulHap::getSolutions() {
//     return;
// }

void GyulHap::playGame() {

}

int main() {
    // Choose number of players and number of rounds
    // cout << "Hello World" << endl;
    Player player1(6);

    cout << player1.getID() << endl;
    cout << player1.getPoints() << endl;
    // GyulHap game1;
    return 0;
}