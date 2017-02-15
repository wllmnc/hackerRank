// Write your Student class here
//https://www.hackerrank.com/challenges/classes-objects
class Student
{
    int scores[5];
    
    public:    
    void input()
    {
        for(int i=0;i<5;i++)
        {
            cin>>scores[i];
        }
    }
    
    int calculateTotalScore()
    {
        int ans=0;
        for(int i=0;i<5;i++)
        {
            ans+=scores[i];
        }
        return ans;
    }
};
