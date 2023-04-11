#include <bits/stdc++.h>
using namespace std;

string rep(string cipher, int key, string sp){
    int index = 0, i = 0;
    int size_sp = sp.length();
    int flag = 0;
    
}

string decryptRailFence(string cipher, int key)
{
    // create the matrix to cipher plain text
    // key = rows , length(text) = columns
    char rail[key][cipher.length()];

    // filling the rail matrix to distinguish filled
    // spaces from blank ones
    for (int i = 0; i < key; i++)
        for (int j = 0; j < cipher.length(); j++)
            rail[i][j] = '\n';

    // to find the direction
    bool dir_down;

    int row = 0, col = 0;

    // mark the places with '*'
    for (int i = 0; i < cipher.length(); i++)
    {
        // check the direction of flow
        if (row == 0)
            dir_down = true;
        if (row == key - 1)
            dir_down = false;

        // place the marker
        rail[row][col++] = '*';

        // find the next row using direction flag
        dir_down ? row++ : row--;
    }

    // now we can construct the fill the rail matrix
    int index = 0;
    for (int i = 0; i < key; i++)
        for (int j = 0; j < cipher.length(); j++)
            if (rail[i][j] == '*' && index < cipher.length())
                rail[i][j] = cipher[index++];

    // now read the matrix in zig-zag manner to construct
    // the resultant text
    string result;

    row = 0, col = 0;
    for (int i = 0; i < cipher.length(); i++)
    {
        // check the direction of flow
        if (row == 0)
            dir_down = true;
        if (row == key - 1)
            dir_down = false;

        // place the marker
        if (rail[row][col] != '*')
            result.push_back(rail[row][col++]);

        // find the next row using direction flag
        dir_down ? row++ : row--;
    }
    return result;
}

// driver program to check the above functions
int main()
{
    string cipher, result;
    int m;

    cin >> m;
    cin >> cipher;

    result = decryptRailFence(cipher, m);

    cout << result << endl;

    size_t index = 0;
    while (true)
    {
        /* Locate the substring to replace. */
        index = result.find("xxx");
        if (index == std::string::npos)
            break;

        /* Make the replacement. */
        result.replace(index, 3, " ");

        /* Advance index forward so the next iteration doesn't pick it up as well. */
        index += 3;
    }
    cout << result;

    return 0;
}
