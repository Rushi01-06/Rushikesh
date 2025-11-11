#include<iostream>
#include<string>
using namespace std;
class complex
{
float real;
float img;
public:
void input()
{
cout<<"enter real part: ";
cin>>real;
cout<<"enter imaginary part: ";
cin>>img;
}
 complex add(complex c){
complex result;
result.real=real+c.real;
result.img=img+c.img;
return result;
}
complex subtract(complex c){
complex result;
result.real=real-c.real;
result.img=img-c.img;
return result;
}
void display() {
cout<<real<<"+"<<img<<"i"<<endl;
}
};
int main() {
complex c1, c2, sum, diff;

cout<<"enter first complex number:\n";
c1.input();

cout<<"enter second comlex number:\n";
c2.input();

sum=c1.add(c2);
diff=c1.subtract(c2);

cout<<"\nfirst number: ";
c1.display();

cout<<"\nsecond number: ";
c2.display();

cout<<"sum: ";
sum.display();

cout<<"diff: ";
diff.display();

return 0;
}



