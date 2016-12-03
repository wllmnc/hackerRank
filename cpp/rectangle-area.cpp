//https://www.hackerrank.com/challenges/rectangle-area
/*
 * Create classes Rectangle and RectangleArea 
 */
class Rectangle{
    public:
        int width , height;
        void display()
        {
            cout<<width<<" "<<height<<"\n";
        }
};
class RectangleArea: public Rectangle{
    public: 
        void read_input(){
            scanf("%d",&width);            
            scanf("%d",&height);
        }
    void display()
        {
            cout<<width*height<<"\n";
        }
};
