#include <iostream>
#include <cstdlib>
#include <ctime>
#include <vector>

#include <bits/stdc++.h>
using namespace std;

class Game {
    private:
        int rounds;
        int players;
    public:
        int getRoundCount();
        int getPlayerCount();
        Game();
};

class Card {
    private:
        vector<int> attributes;

    public:
        Card(vector<int> array);

        vector<int> getAttributes();
        void printAttributes();
        Card findThirdCard(Card otherCard);
};

class Board {
    private:
        vector<Card> cards;
        vector<vector<Card>> solutions;
    public:
        vector<Card> getCards();
        vector<vector<Card>> getSolutions();
        void generateCards(int amount, int traits);
        void findSolutions();
        void displayCards(int length, int width);
        // vector<Card> drawCards();
        Board(int amount, int traits);
};

Board::Board(int amount, int traits) {
    this->generateCards(amount, traits);
    // this->findSolutions();
}

vector<Card> Board::getCards() {
    return this->cards;
}

vector<vector<Card>> Board::getSolutions() {
    return this->solutions;
}

void Board::generateCards(int amount, int traits) {
    vector<int> values;

    for (int i = 0; i < amount; i++) {
        for (int i = 0; i < traits; i++) {
            int randomNum = rand() % 3;
            values.push_back(randomNum);
        }

        Card newCard(values);
        (this->cards).push_back(newCard);

        values.clear();
    }
}

void Board::findSolutions() {
    vector<Card> set;
    vector<Card> visited;

    for (int i = 0; i < this->getCards().size(); i++) {
        for (int j = i + 1; j < this->getCards().size(); j++) {
            Card search = (this->getCards()).at(i).findThirdCard(this->getCards().at(j));

            cout << "First Card: ";
            (this->getCards()).at(i).printAttributes();
            cout << endl;

            cout << "Second Card: ";
            (this->getCards()).at(j).printAttributes();
            cout << endl;

            cout << "Resulting Card: ";
            search.printAttributes();
            cout << endl;

            // auto it = find(visited.begin(), visited.end(), search);
            // if (it != visited.end()) {

            // }
        }

        // I have to define the push back function for Card vectors
        // visited.push_back();
    }
}

void Board::displayCards(int length, int width) {
    for (int i = 0; i < length; i++) {
        for (int j = 0; j < width; j++) {
            (cards.at(i*length + j)).printAttributes();
            cout << " ";
        }
        cout << endl;
    }
}

Card::Card(vector<int> array) {
    this->attributes = array;
}

vector<int> Card::getAttributes() {
    return this->attributes;
}

void Card::printAttributes() {
    cout << "(";
    for (int i = 0; i < this->getAttributes().size(); i++) {
        cout << this->getAttributes().at(i);
    }
    cout << ")";
}

Card Card::findThirdCard(Card otherCard) {
    int value;
    vector<int> newAttributes;

    for (int i = 0; i < this->getAttributes().size(); i++) {
        value = ((this->getAttributes().at(i) * -1) + (otherCard.getAttributes().at(i) * -1) + 6) % 3;
        newAttributes.push_back(value);
    }

    return Card(newAttributes);
}

int main() {
    srand(time(0));
    Card card1({0, 1, 0});
    Card card2({2, 1, 0});

    // card1.printAttributes();
    // card2.printAttributes();

    // Card result = card1.findThirdCard(card2);
    // result.printAttributes();

    Board gameBoard(9, 3);
    gameBoard.displayCards(3, 3);
    gameBoard.findSolutions();

    return 0;
}