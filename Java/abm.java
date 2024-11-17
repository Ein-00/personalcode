import java.util.*;

public class abm{
    public static void main(String[] args){
        square s = new square(2);
        s.calculatearea();
        s.display_area();
       square.test();
    }
}
abstract class shape{
    float area;
    public shape(){
        this.area = 0.0F;
    }
    abstract public void calculatearea();
    public static void test(){
        System.out.println("Hello from static method.");
    }
    public final void display_area(){
        System.out.println(area);
        
    }
}
class square extends shape{
    int side;
    public square(int side){
        this.side= side;
    }
    public void calculatearea(){
        this.area = side*side;
    }
}
