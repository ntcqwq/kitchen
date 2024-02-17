#include <iostream>
#include <string>

int main() {
    std::string word;
    std::cin >> word;

    for (int i = 0; i < word.length(); i++) {
        if (word[i] != 73 && word[i] != 79 && word[i] != 83 && word[i] != 72 && word[i] != 90 && word[i] != 88 && word[i] != 78) {
            std::cout << "NO";
            break;
        }
        if (i == word.length() - 1) {
            std::cout << "YES";
        }
    }
    return 0;
}