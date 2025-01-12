#include <iostream>
#include <vector>
using namespace std;

class Card {
    private:
        vector<int> attributes;

    public:
        Card(vector<int> array);

        vector<int> getAttributes();
        Card findThirdCard(Card otherCard);
};

Card::Card(vector<int> array) {
    this->attributes = array;
}

vector<int> Card::getAttributes() {
    return this->attributes;
}

Card Card::findThirdCard(Card otherCard) {
    int value;
    vector<int> newAttributes;

    for (int i = 0; i < this->attributes.size(); i++) {
        value = ((this->getAttributes().at(i) * -1) + (otherCard.getAttributes().at(i) * -1) + 6) % 3;
        newAttributes.push_back(value);
    }

    return Card(newAttributes);
}

int main() {
    Card card1({0, 1, 1});
    Card card2({2, 2, 2});

    Card result = card1.findThirdCard(card2);

    return 0;
}