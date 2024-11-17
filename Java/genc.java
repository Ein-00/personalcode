class Student{
  int i;
  Student(int i){
    this.i = i;
  }
}
class Gen<T extends Student>{
  T o;
  Gen(T o){
    this.o = o;
  }
  void showtype(){
    System.out.println(o.getclass().getName());
  }
}
class genc{
  public static void main(String[] args){
    Gen<Student> ob = new Gen<>(new Student(5));
    ob.showtype();
  }
}
