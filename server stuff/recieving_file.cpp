#include <iostream>

using namespace std;

#define sum(x,y) x+y

inline int diff(int x, int y) { return (x-y); }

int main()
{
    int a = sum(8,3) * sum(8,3);
    int b = diff(8,3) * diff(8,3);

    cout<<sum(8,3)<<endl;

    cout<<a<<b;
    return 0;
}