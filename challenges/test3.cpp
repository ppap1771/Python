#include<bits/stdc++.h>
using namespace std;

void solve(string alpha, int x, int y, string cipher){
    char alphabet[3][10];
    int k = 0;
    for(int i = 0; i < 3 ; i++){
        for(int j = 0; j < 10; j++){
            if((i == 0) && ((j == x) or (j == y))){
                alphabet[i][j] = '?';
            }
            else{
                alphabet[i][j] = alpha[k++];
            }
        }
    }

    // disp
    // for(int i = 0; i < 3 ; i++){
    //     for(int j = 0; j < 10; j++){
    //         cout << alphabet[i][j] << " ";
    //     }
    //     cout << "\n";
    // }


    int len = cipher.length();
    // int arr[len];
    // for(int i = 0; i < len; i++){
    //     arr[i] = cipher[i] - '0';
    // }

    string plain_text = "";
    for(int i = 0; i < len; i++){
        if(((int)cipher[i] - 48) == x){
            plain_text += alphabet[1][((int)cipher[i+1] - 48)];
            // cout << alphabet[1][(int)cipher[i+1]] << "\n";
            i++;
        }
        else if(((int)cipher[i] - 48) == y){
            plain_text += alphabet[2][((int)cipher[i+1] - 48)];
            // cout << alphabet[2][(int)cipher[i+1]] << "\n";
            i++;
        }
        else{
            plain_text += alphabet[0][((int)cipher[i] - 48)];
            // cout << alphabet[0][(int)cipher[i]] << "\n";
        }
    }   

    cout << plain_text << "\n";
}

int main(){
    int x, y;
    string alpha;
    string cipher;

    cin >> alpha;
    cin >> x >> y;
    cin >> cipher;

    // cout << cipher << "\n";
    solve(alpha, x, y, cipher);
    return 0;
}