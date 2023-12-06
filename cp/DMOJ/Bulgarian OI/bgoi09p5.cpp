#include <bits/stdc++.h>

using namespace std;

#define endl "\n";
#define fastio ios_base::sync_with_stdio(false); cin.tie(nullptr); cout.tie(nullptr);

const int inf = numeric_limits<int>::max();

vector<long long> snum;

long long s7(int c) {
    return stoll("7" + string(c, '0'));
}

vector<long long> s97(int c) {
    vector<long long> seq;
    int count = c - 1;
    while (count != -1) {
        seq.push_back(stoll(string(c - 1 - count, '9') + "97" + string(count, '0')));
        count--;
    }
    return seq;
}

vector<long long> s2(int c) {
    vector<long long> seq;
    if (c == 1) {
        return seq;
    } else if (c == 2) {
        seq.push_back(2120);
        return seq;
    } else {
        c -= 1;
        int digits = c + 3;
        int nums = c / 2;
        if (c % 2 == 0) {
            seq.push_back(stoll("2" + string((digits - 3) / 2, '0') + "1" + string((digits - 3) / 2, '0') + "2"));
            for (int i = 1; i < nums; i++) {
                seq.push_back(stoll("2" + string((digits - 3) / 2 - i, '0') + "1" + string((digits - 3) / 2 - i, '0') + "2" + string(2 * i, '0')));
            }
        } else {
            seq.push_back(stoll("2" + string((digits - 3) / 2, '0') + "1" + string((digits - 3) / 2, '0') + "2" + "0"));
            for (int i = 1; i < nums; i++) {
                seq.push_back(stoll("2" + string((digits - 3) / 2 - i, '0') + "1" + string((digits - 3) / 2 - i, '0') + "20" + string(2 * i, '0')));
            }
        }
        seq.push_back(stoll("212" + string(c, '0')));
        return seq;
    }
}

vector<long long> s3(int c) {
    vector<long long> seq;
    if (c == 1) {
        return seq;
    } else {
        if (c > 4) {
            seq.push_back(stoll("3074003" + string(c - 5, '0')));
        }
        seq.push_back(stoll("3148" + string(c - 2, '0')));
        return seq;
    }
}

int main() {
	fastio;
    int N;
    cin >> N;

    int cycle = 1;
    while (snum.size() <= N) {
        snum.push_back(s7(cycle));

        vector<long long> s97_seq = s97(cycle);
        snum.insert(snum.end(), s97_seq.begin(), s97_seq.end());

        vector<long long> s2_seq = s2(cycle);
        snum.insert(snum.end(), s2_seq.begin(), s2_seq.end());

        vector<long long> s3_seq = s3(cycle);
        snum.insert(snum.end(), s3_seq.begin(), s3_seq.end());

        cycle++;
    }

    for (int i = 0; i < 5; i++) {
        snum.push_back(953671853653 * static_cast<long long>(pow(10, i)));
        snum.push_back(2118984413357 * static_cast<long long>(pow(10, i)));
        snum.push_back(2121179131852 * static_cast<long long>(pow(10, i)));
    }
    snum.push_back(95367185365300000);
    snum.push_back(6328428636000007);
    snum.push_back(63284286360000070);
    snum.push_back(99704560597822753);

    sort(snum.begin(), snum.end());

    cout << snum[N - 1] << endl;

    return 0;
}