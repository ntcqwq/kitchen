#include <bits/stdc++.h>

using namespace std;

#define endl "\n";
#define fastio ios_base::sync_with_stdio(false); cin.tie(nullptr);

typedef long long ll;
const int inf = 1e6+1;

#define N 8

int board[N][N], mark[N][N];

void placeOnBoard(int i, int j){
    int count = 0;
    if(mark[i][j] == 0) mark[i][j] = 1;
    if(i+2 < N && j+1 < N && mark[i+2][j+1] == 0) mark[i+2][j+1] = 1;
    if(i+2 < N && j-1 >= 0 && mark[i+2][j-1] == 0) mark[i+2][j-1] = 1;
    if(i-2 >= 0 && j+1 < N && mark[i-2][j+1] == 0) mark[i-2][j+1] = 1;
    if(i-2 >= 0 && j-1 >= 0 && mark[i-2][j-1] == 0) mark[i-2][j-1] = 1;

    if(j+2 < N && i+1 < N && mark[i+1][j+2] == 0) mark[i+1][j+2] = 1;
    if(j+2 < N && i-1 >= 0 && mark[i-1][j+2] == 0) mark[i-1][j+2] = 1;
    if(j-2 >= 0 && i+1 < N && mark[i+1][j-2] == 0) mark[i+1][j-2] = 1;
    if(j-2 >= 0 && i-1 >= 0 && mark[i-1][j-2] == 0) mark[i-1][j-2] = 1;
}

void printBoard(){
    for(int i = 0;i < N;i++){
        for(int j = 0;j < N;j++){
            if(board[i][j] != 0) cout << "K ";
            else cout << board[i][j] << " ";
        }
        cout << endl;
    }
    cout << endl;
}

void backtrackBlack(int knightNum, int currX, int currY){
    if(knightNum == 7){
        int count = 0;
        for(int i = 0;i < N;i++) for(int j = 0;j < N;j++) mark[i][j] = 0;
        for(int i = 0;i < N;i++){
            for(int j = 0;j < N;j++) if(board[i][j] != 0) placeOnBoard(i, j);
        }
        for(int i = 0;i < N;i++){
            for(int j = 0;j < N;j++) if(mark[i][j] != 0) count++;
        }
        if(count == 64) printBoard();
        return;
    }
    if(currX == N-1 && currY == N) return;
    int newX, newY;     //new place in the board to move to
    if(currY == N) newY = 0,newX = currX + 1;
    else newY = currY + 1,newX = currX;

    //do not place the current knight at (currX, currY)
    backtrackBlack(knightNum, newX, newY);
    //try to place the current knight at (currX, currY)
    if((currX + currY) % 2 == 1 && currX > 0 && currX < N-1 && currY > 0 && currY < N-1){
        board[currX][currY] = knightNum;
        backtrackBlack(knightNum+1, newX, newY);
        board[currX][currY] = 0;
    }
}

void backtrackWhite(int knightNum, int currX, int currY){
    if(knightNum == 7){
        int count = 0;
        for(int i = 0;i < N;i++) for(int j = 0;j < N;j++) mark[i][j] = 0;
        for(int i = 0;i < N;i++){
            for(int j = 0;j < N;j++) if(board[i][j] != 0) placeOnBoard(i, j);
        }
        for(int i = 0;i < N;i++){
            for(int j = 0;j < N;j++) if(mark[i][j] != 0) count++;
        }
        if(count >= 32){
            backtrackBlack(1, 0, 0);
            //printBoard();
        }
        return;
    }
    if(currX == N-1 && currY == N) return;
    int newX, newY;     //new place in the board to move to
    if(currY == N) newY = 0,newX = currX + 1;
    else newY = currY + 1,newX = currX;

    //do not place the current knight at (currX, currY)
    backtrackWhite(knightNum, newX, newY);
    //try to place the current knight at (currX, currY)
    if((currX + currY) % 2 == 0 && currX > 0 && currX < N-1 && currY > 0 && currY < N-1){
        board[currX][currY] = knightNum;
        backtrackWhite(knightNum+1, newX, newY);
        board[currX][currY] = 0;
    }
}

int main(){
    time_t t = clock();
    backtrackWhite(1, 0, 0);
    printBoard();
    return 0;
}