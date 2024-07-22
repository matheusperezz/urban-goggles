#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include "utils.h"

using namespace std;

void printMessage()
{
    cout << "This is a message from the utils file!" << endl;
}

void c_221()
{
    int N1, N2, N3;
    cin >> N1;
    cin.ignore();

    string temp;
    getline(cin, temp);
    stringstream ss1(temp);

    vector<string> m_professor;
    string item;
    while (ss1 >> item)
    {
        m_professor.push_back(item);
    }

    cin >> N2;
    cin.ignore();

    getline(cin, temp);
    stringstream ss2(temp);
    vector<string> m_blocked;
    while (ss2 >> item)
    {
        m_blocked.push_back(item);
    }

    cin >> N3;
    cin.ignore();

    getline(cin, temp);
    stringstream ss3(temp);
    vector<string> m_querys;
    while (ss3 >> item)
    {
        m_querys.push_back(item);
    }

    for (const auto& query : m_querys)
    {
        if (find(m_blocked.begin(), m_blocked.end(), query) != m_blocked.end())
        {
            cout << "Proibido" << endl;
        } else
        {
            cout << "Geral" << endl;
        }
    }

}