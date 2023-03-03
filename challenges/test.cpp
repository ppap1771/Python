#include <bits/stdc++.h>
using namespace std;

string kw, cipher, encrypt;
char polyb_square[5][5];

string parse(string answer){
    int n = answer.length();
    // cout << n << "\n";
    string final = "";
    int k = 0;
    for(int i = 0; i < n; i++){
        if(answer[i] != '?'){
            final += answer[i];
            k++;
        }  
    }

    return final;
}

string concat(string en_text, char a)
{
    // pointing to the index of the last character of x
    en_text += a;
    return (string)en_text;
}

string ct2(string en_text){
    // string s_kw = sort(kw);
    int n1 = kw.length();
    int n2 = (en_text.length()%n1 == 0)?(en_text.length()/n1) : ((en_text.length()/n1) + 1);

    // cout << n1 << " " << n2 << "\n";

    char t2[n2][n1];
    int k = 0, itr = 0;
    for(int i = 0; i < n2; i++){
        for (int j = 0; j < n1; j++)
        {
            /* code */
            if(i==0){
                t2[i][j] = kw[k];
                k++;
            }
            if (itr < en_text.length())
            {
                t2[i][j] = en_text[itr];
                itr++;
            }
            else
            {
                t2[i][j] = '?';
            }
        }
        
    }

    // for (int i = 0; i < n2; i++)
    // {
    //     for (int j = 0; j < n1; j++)
    //     {
    //         cout << t2[i][j] << " ";
    //     }
    //     cout << "\n";
    // }
    string kw_t = kw;
    sort(kw_t.begin(), kw_t.end());

    // cout << kw_t << "\n"; 
    string en_text1 = "";

    for(int i = 0; i < n1; i++){
        char t1 = kw_t[i];
        for(int j = 0; j < n1; j++){
            // cout << t1 << " " << kw[j] << " " << i << " " << j << "\n";
            if(t1 == kw[j]){
            
                for(int k = 0; k < n2; k++){
                    // cout << t2[k][j] << "\n";
                    en_text1 = concat(en_text1, t2[k][j]);
                }
            }
        }
    }

    return en_text1;
}

string ct1()
{
    int size = encrypt.length();
    string test_bench = "ADFGX";
    string en_text = "\0";
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            for (int k = 0; k < 5; k++)
            {
                // cout << encrypt[i] << " " << polyb_square[j][k] << "\n";
                if (encrypt[i] == polyb_square[j][k])
                {
                    en_text = concat(en_text, test_bench[j]);
                    en_text = concat(en_text, test_bench[k]);
                    // cout << en_text << "\n";
                }
            }
        }
    }
    return en_text;
}

void print_mat(char mat[5][5])
{
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            cout << mat[i][j] << " ";
        }
        cout << "\n";
    }
}

void polyb_squar_gen(string cipher)
{

    int i, j, k = 0;
    for (i = 0; i < 5; i++)
    {
        for (j = 0; j < 5; j++)
        {
            polyb_square[i][j] = cipher[k];
            k++;
        }
    }

    // print_mat(polyb_square);
}

void solve()
{
    polyb_squar_gen(cipher);
    string text1 = ct1();

    // cout << text1 << "\n";

    string text2 = ct2(text1);
    text2 = parse(text2);
    cout << text2 << "\n";
    return;
}

int main()
{
    cin >> kw;
    cin >> cipher;
    cin >> encrypt;

    // cout << kw << "\n";
    // cout << cipher << "\n";
    // cout << encrypt << "\n";

    solve();
    return 0;
}
