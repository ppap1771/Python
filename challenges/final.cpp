#include <bits/stdc++.h>
using namespace std;

string decryptRailFence(string cipher, int key)
{
    int size = cipher.length();
    char rail[key][cipher.length()];

    for (int i = 0; i < key; i++)
        for (int j = 0; j < size; j++)
            rail[i][j] = '\n';

    int Downlink;

    int row = 0, col = 0;

    for (int i = 0; i < cipher.length(); i++)
    {

        if (row == 0)
            Downlink = 1;
        if (row == key - 1)
            Downlink = 0;

        rail[row][col++] = '*';

        (Downlink == 1) ? row++ : row--;
    }

    int c = 0;
    for (int i = 0; i < key; i++)
        for (int j = 0; j < cipher.length(); j++)
            if (rail[i][j] == '*' && c < cipher.length())
                rail[i][j] = cipher[c++];

    string final;

    row = 0, col = 0;
    for (int i = 0; i < cipher.length(); i++)
    {

        if (row == 0)
            Downlink = 1;
        if (row == key - 1)
            Downlink = 0;

        // place the marker
        if (rail[row][col] != '*')
            final.push_back(rail[row][col++]);

        (Downlink == 1) ? row++ : row--;
    }
    return final;
}

string decrypt(string cipher, int key)
{

    char rail[key][cipher.length()][100];

    for (int i = 0; i < key; i++)
        for (int j = 0; j < cipher.length(); j++)
            rail[i][j][0] = '-';

    int Downlink;

    int row = 0, col = 0;
    int numSpace = 0;
    for (int i = 0; i < cipher.length(); i++)
    {
        if (cipher[i] == ' ')
            numSpace++;
    }

    for (int i = 0; i < numSpace; i++)
    {

        if (row == 0)
            Downlink = 1;
        if (row == key - 1)
            Downlink = 0;

        rail[row][col++][0] = '*';

       (Downlink==1) ? row++ : row--;
    }

    int c = 0;
    for (int i = 0; i < key; i++)
    {
        for (int j = 0; j < cipher.length(); j++)
        {
            string a = "";
            if (rail[i][j][0] == '*' && c < cipher.length())
            {
                while (1)
                {
                    a += cipher[c];
                    if (cipher[c] == ' ')
                    {
                        c++;
                        break;
                    }
                    c += 1;
                }
                for (int k = 0; k < a.length(); k++)
                {
                    rail[i][j][k] = a[k];
                }
            }
        }
    }

    string final;

    row = 0, col = 0;
    for (int i = 0; i < cipher.length(); i++)
    {

        if (row == 0)
            Downlink = 1;
        if (row == key - 1)
            Downlink = 0;

        if (rail[row][col][0] != '*')
            for (int k = 0; k < 20; k++)
            {
                final.push_back(rail[row][col][k]);
                if (rail[row][col][k] == ' ')
                    break;
            }
        col++;

        (Downlink == 1) ? row++ : row--;
    }
    string a = "";
    for (int k = 0; k < cipher.length() - 1; k++)
    {
        a += final[k];
    }
    return a;
}

int main()
{
    int N, n, M, m = 0;
    cin >> N;
    cin >> n;
    cin >> M;
    cin >> m;
    cin.ignore();

    string X;
    cin >> X;
    cin.ignore();

    string message;
    getline(cin, message);

    for (int i = 0; i < M; i++)
        message = decryptRailFence(message, m);

    string replace_with = " ";

    size_t pos = 0;
    while ((pos = message.find(X, pos)) != string::npos)
    {
        message.replace(pos, X.length(), replace_with);
        pos += replace_with.length();
    }
    int numSpace = 0;
    for (int i = 0; i < message.length(); i++)
    {
        if (message[i] == ' ')
            numSpace++;
    }

    message += " ";

    string b = message;
    for (int i = 0; i < N; i++)
    {
        b = decrypt(b, n);
        b += " ";
    }

    cout << b;

    return 0;
}
