#include <iostream>
#include <string>

using namespace std;

int main() {
    string sentence;
    int h = 0, s = 0;

    getline(cin, sentence);

    for (int i = 0; i < sentence.length() - 1; i++) {
        if (sentence[i] == ':' && sentence[i+1] == '-') {
            if (i+2 < sentence.length() && sentence[i+2] == ')') {
                h++;
            } else if (i+2 < sentence.length() && sentence[i+2] == '(') {
                s++;
            }
        }
    }

    if (h == 0 && s == 0) {
        cout << "none" << endl;
    } else if (h == s) {
        cout << "unsure" << endl;
    } else if (h > s) {
        cout << "happy" << endl;
    } else {
        cout << "sad" << endl;
    }

    return 0;
}