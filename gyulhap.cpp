#include <iostream>

void printBoard(int gameBoard[][3], int size) {
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            std::cout << gameBoard[i][j] << std::endl;
        }
    }
}

int main() {
    std::cout << "Hello World" << std::endl;

    int gameBoard[3][3] = {{123,123,123},
                           {123,123,123},
                           {123,123,123}};
    
    printBoard(gameBoard, 3);

    return 0;
}