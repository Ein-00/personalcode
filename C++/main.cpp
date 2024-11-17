#include <iostream>
#include <string>
using namespace std;


template <typename T>
T smaller(T first , T second){
    return (first < second) ? first : second;
}

int main(){
    int first ,second;
    cout << "Enter the first number" <<endl;
    cin >> first;
    cout << "Enter the second number" << endl;
    cin  >> second;
    cout << smaller(first,second) <<endl;
    string s1 , s2;
    cin.ignore();
    cout << "Enter the first name" << endl;
    getline(cin , s1);
    cout << "Enter the second name" << endl;
    getline(cin , s2);
    cout << "S1" << s1 << endl;
    cout << "S2" << s2 << endl;
    cout << smaller(s1, s2) << endl;


}
