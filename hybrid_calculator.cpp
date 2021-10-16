#include <iostream>
#include <cmath>
using namespace std;

class simple_calculator
{
    int a, b;

    public:
    void getDATAsimple()
    {

        cout << "Enter the first number: " << endl;
        cin >> a;
        cout << "Enter the second number: " << endl;
        cin >> b;
    }
    void perform_simple_calc()
    {
            cout<<"The value of a + b is: "<<a + b<<endl;
            cout<<"The value of a - b is: "<<a - b<<endl;
            cout<<"The value of a * b is: "<<a * b<<endl;
            cout<<"The value of a / b is: "<<a / b<<endl;
    }
};
class scientific_calculator
{
    int a, b;

    public:
    void getDATAscientific()
    {

        cout << "Enter the first number: "<<endl;
        cin >> a;
        cout << "Enter the second number: "<<endl;
        cin >> b;
    }
    void perform_scientific_calc()
    {
        cout << "the value of sin (" << a << ") is: " << sin(a) << endl;
        ;
        cout << "the value of cos (" << a << ") is: " << cos(a) << endl;
        ;
        cout << "the value of tan (" << a << ") is: " << tan(a) << endl;
        ;
        cout << "the value of log (" << a << ") is: " << log(a) << endl;
        ;
        cout << "the value of exp (" << a << ") is: " << exp(a) << endl;
        ;
    }
};
class hybridCalculator : public simple_calculator, public scientific_calculator
{
};

int main()
{
    //   simple_calculator cal;
    //   scientific_calculator calc;
    //   cal.getDATAsimple();
    //   cal.perform_simple_calc();

    hybridCalculator hcalc;
    hcalc.getDATAsimple();
    hcalc.perform_simple_calc();
    hcalc.getDATAscientific();
    hcalc.perform_scientific_calc();
    
     return 0;
}