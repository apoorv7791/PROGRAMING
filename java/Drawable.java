interface Drawable {
    void draw(); 
}
//implementation of the second user
class Rectangle implements Drawable{
    public void draw()
    {
        System.out.println("User is drawing ");
    }
}
class Circle implements Drawable{
    public void draw()
    {
        System.out.println("Drawing something else");
    }
}
class TestInterface{
    public static void main(String[] args) {
        Drawable f = new Circle();
        f.draw();
    }
}