#include<bits/stdc++.h>
using namespace std;

void solve(int key, string cipher){
    int row = cipher.length() / key;
    int column = key;
    int n = cipher.length();
    char decode[row][column];
    int pos[2] = {0, 0};
    // decode = new char *[column];
    int k = 0;
    for(int i = 0; i < n; i++){
        decode[pos[0]][pos[1]] = cipher[i];
        pos[0] += 1;
        pos[1] = (pos[1] + 2) % column;
        
        if(pos[0] == row){
            pos[0] = 0;
            pos[1] = ++k;
        }
    }
    // disp
    // 00 01 02
    for(int i = 0; i < row; i++){
        for(int j = 0; j < column;j++){
            cout << decode[i][j];
        }
    }
    cout << "\n";
}

int main(){
    int key;
    string cipher;

    cin >> key;
    cin >> cipher;
    
    solve(key, cipher);
}