#include<iostream>
using namespace std;
class Banking_System{
    public :
    float Balance = 0 ;
    float Deposit;
    float Withdrawl;

int Total_Deposit(float n){
    this->Balance += n;
    return this->Balance;

}

int Total_Withdrawl(float a){
    if(a>this->Balance){
        cout<<"not sufficient balance";
    }
    else{
    this->Balance -=a ;
    return this->Balance;}
}

void Total_Balance(){
    if(this->Balance <0){
        cout<<" need to pay money to bank";
    }
    cout<<this->Balance;
    
}
};    


int main(){
    Banking_System s1;
   s1.Total_Deposit(600);
   s1.Total_Withdrawl(90);
   s1.Total_Deposit(6000);
   s1.Total_Withdrawl(900);
   s1.Total_Balance();

   

}