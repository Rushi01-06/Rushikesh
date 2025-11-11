#include<iostream>
#include<string>

using namespace std;
class student
{
private:
 int roll_no;
 int marks;
 string name;
public:
void input(){
cout<<"enter roll no: ";
cin>>roll_no;
cout<<"enter marks: ";
cin>>marks;
cout<<"enter name: ";
cin>>name;
}
void display()
{
cout<<"roll no is: "<< roll_no<<endl;
cout<<"marks is: "<<marks<<endl;
cout<<"student name: "<<name;
}
};
int main()
{
student s;
s.input();
s.display(); 
return 0;
}
