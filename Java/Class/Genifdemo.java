package Class;
//A generic interface example
interface MinMax <T extends Comparable<T>>{
    T min();
    T max();
}
//Implementation of minmax using implements
class MyClass <T extends Comparable <T>> implements MinMax<T>{
    T[] vals;
    MyClass(T[] o ){
        vals = o;
    }
    public T min(){
        T v = vals[0];
        for(int i = 1;i< vals.length;i++){
            if(vals[i].compareTo(v) < 0){
                v = vals[i];
            }
            
        }
        return v;
    }
    public T max(){
        T v = vals[0];
        for(int i =1;i <vals.length;i++){
            if(vals[i].compareTo(v) > 0){
                v = vals[i];
            }

        }
        return v;
    }
}
class Genifdemo{
    public static void main(String[] args){
        Integer I[] = {3,6,2,8,6};
        Character c[] = {'b','r', 'p','w'};
        MyClass<Integer> iob= new MyClass<Integer>(I);
        MyClass<Character> cob= new MyClass<Character>(c);
        System.out.println(iob.max());
        System.out.println(iob.min());
        System.out.println(cob.max());
        System.out.println(cob.min());
                


    }
}