#include <iostream>
#include <vector>
using namespace std;

class Card {
    private:
        int shape;
        int colour;
        int background;

    public:
        int getShape();
        int getColour();
        int getBackground();
        bool isSet(Card otherCard);
        Card(int shape, int colour, int background);
};

Card::Card(int shape, int colour, int background) {
    this->shape = shape;
    this->colour = colour;
    this->background = background;
}

bool Card::isSet(Card otherCard) {
    cout << "This card is (" << getShape() << ", " << getColour() << ", " << getBackground() << ")" << endl;
    cout << "Other card is (" << otherCard.getShape() << ", " << otherCard.getColour() << ", " << otherCard.getBackground() << ")" << endl;
    return true;
}

int Card::getShape() {
    return this->shape;
}

int Card::getColour() {
    return this->colour;
}

int Card::getBackground() {
    return this->background;
}

int main() {
    cout << "Hello World" << endl;
    Card card1(1, 2, 3);
    Card card2(3, 4, 5);

    card1.isSet(card2);
    card2.isSet(card1);

    return 0;
}