#include <iostream>
#include <string>
#include <sstream>
#include <windows.h>
#include <fstream>
using namespace std;



class Login{
    private:
    string LoginID,password;
    public:
    Login():LoginID(""),password(""){}


    void SetID(string id){
        LoginID = id;
    }
    void SetPass(string pass){
        password = pass;
    }
    
    string getID(){
        return LoginID;
    }
    string getPass(){
        return password;
    }
};
int registration(Login log){
    system("cls");
    string id,password;
    cout<<"\tEnter login id"<<endl;
    cin >>id;
    log.SetID(id);
    start:
    cout <<"\tEnter password " <<endl;
    cin >> password;
    if(password.length()  >= 8){
        log.SetPass(password);
    }
    else{
        cout<<"\t Enter minimum 8 characters" <<endl;
        goto start;
    }
    ofstream outfile("C:/Users/SRINIVAS  KULAL/Documents/Login.txt" , ios::app);
    if(!outfile){
        cout << "Error file cannot open"<< endl;

    }
    else{
        outfile <<"\t"<<log.getID() <<" : "<<log.getPass()<<endl<<endl;
        cout <<"Registration successful"<<endl;
    }
    outfile.close();
    Sleep(1000);

}



void login(){
    system("cls");
    string id, password; 
    cout << "\t Enter your Login ID"<<endl;
    cin >> id;
    cout << "\t Enter your password"  <<endl;
    cin >> password;
    ifstream infile("C:/Users/SRINIVAS  KULAL/Documents/Login.txt");
    if(!infile){
        cout << "Error file cannot open"<<endl;
    }
    else{
        string line;
        bool found = false;
        while(getline(infile, line)){
            stringstream ss;
            ss << line ;
            string userid , userpass;
            char delimiter;
            ss >>userid>>delimiter>>userpass;


            if(id == userid && password ==userpass){
                found = true;
                system("cls"); 
                cout << "\tWelcome to this page" <<endl;

            }
        }
        if(!found){
            cout << "\t Error :Incorrect Login ID or password"<<endl;
        }
    
    }
    infile.close();
    Sleep(1000);
}
int main(){
    Login log;
    bool exit = false;

    while(!exit){
        system("cls");
        int val;
        cout << "\tWelcome To Registration & Login form"<<endl;
        cout << "\t************************************"<<endl;
        cout << "\t1.Register"<<endl;
        cout << "\t2.Login"<<endl;
        cout << "\t3.Exit"<<endl;
        cout << "\tEnter your choice"<<endl;
        cin >> val ;
        Sleep(1000);


        if (val == 1){
            registration(log);
        } 
        else if (val == 2){
            login();
        }
        else if(val == 3){
            exit = true;
            cout << "Exiting" <<endl;
        }



        
    }
}

