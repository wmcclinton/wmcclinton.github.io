#include <iostream>
using namespace std;

template <class T>
class Account {
    public:
        T data;
};

template <class T>
class cAccount : public Account<T> {
    public:
        T cdata;
};

int main() 
{
    cout << "Hello, World!";
    return 0;
}