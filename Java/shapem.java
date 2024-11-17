import java.util.*;

public class shapem{
    public static void main(String [] args){
        shape s[] = new shape[5];
        s[0] = new circle();
        s[1] = new rectangle();
        s[2] = new square();
        s[3] = new hexagon();
        s[4] = new polygon();
        for(int i = 0;i<s.length;i++){
            s[i].display_shape();
        }


    }

}
class shape{
    public void display_shape(){
        System.out.println("Shape");
    }
}
class circle extends shape{
    @Override
    public void display_shape(){
        System.out.println("Circle");
    }
}
class rectangle extends shape{
    @Override
    public void display_shape(){
        System.out.println("Rectangle");
    }

}
class square extends shape{
    @Override
    public void display_shape(){
        System.out.println("Square");
    }
} 
class hexagon extends shape{
    public void display_shape(){
        System.out.println("Hexagon");
    }
}
class polygon extends shape{
    public void display_shape(){
        System.out.println("Polygon");
    }

}
