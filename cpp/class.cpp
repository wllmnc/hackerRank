//https://www.hackerrank.com/challenges/c-tutorial-class
#include <iostream>
#include <sstream>

using namespace std;

class Student
{
    private:
        int age,standard;
        string first_name, last_name;
    public:
    int     get_age()                    {return age;}
    void    set_age(int age_)            {age=age_;} 
    string  get_first_name()             {return first_name;}
    void    set_first_name(string first_){first_name=first_;}
    string  get_last_name()              {return last_name;}
    void    set_last_name(string last_)  {last_name=last_;}
    int     get_standard()               {return standard;}
    void    set_standard(int standard_)  {standard=standard_;}
    string  to_string()                  {return std::to_string(age)+","+first_name+","+last_name+","+std::to_string(standard);}
};

int main() {
    int age, standard;
    string first_name, last_name;
    
    cin >> age >> first_name >> last_name >> standard;
    
    Student st;
    st.set_age(age);
    st.set_standard(standard);
    st.set_first_name(first_name);
    st.set_last_name(last_name);
    
    cout << st.get_age() << "\n";
    cout << st.get_last_name() << ", " << st.get_first_name() << "\n";
    cout << st.get_standard() << "\n";
    cout << "\n";
    cout << st.to_string();
    
    return 0;
}
