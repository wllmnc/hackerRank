#include <math.h>  
// Create the classes here.
class Circle{
    private:
        float radius;
    public:
        Circle(float _radius)
        {
            radius=_radius;
        }
        int getArea()
        {
            return ceil(3.1416*radius*radius);
        }
};
class Rectangle{
    private:
        float width, height;
    public:
        Rectangle(float _width, float _height)
        {
            width=_width;
            height=_height;
        }
        int getArea()
        {
            return ceil(width*height);
        }
};
class Square{
    private:
        float width;
    public:
        Square(float _width)
        {
            width=_width;
        }
        int getArea()
        {
            return ceil(width*width);
        }
};
