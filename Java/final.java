import java.util.*; 





public class jfinal{
    public static void main(String [] args){
        btechstudent s = new btechstudent();
        s.display_btech();

    }
     
}
class student{
    protected final String univer;
    public student(){
        univer = "MIT manipal";
    }
    public void display_student(){
        System.out.println(univer);
    }

}
class btechstudent extends student{
    univer = "MAHE";
    public void display_btech(){
        System.out.println(this.univer);
    }
    }
