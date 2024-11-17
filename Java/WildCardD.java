class Stats<T extends Number>{
    T[] Nums;
    Stats( T[] o){
        Nums = o;
    }
    double average(){
        double sum = 0.0;
        for(int i = 0 ;i<Nums.length;i++){
            sum+= Nums[i].doubleValue();
        
            
        }
        return sum/Nums.length;

    }
    boolean SameAVG(Stats<?> ob){ // results in error  Stats<Double> cannot be converted to Stats<Integer>
        if(average() == ob.average()){
            return true;
        }
        return false;
    }
}


public class WildCardD {
    public static void main(String[] args) {
        Integer iarr[] = {1,2,3,4,5};
        Stats<Integer> iob = new Stats<Integer>(iarr);
        double v= iob.average();
        System.out.println(v);
        Double darr[] = {1.1,2.2,3.3,4.4,5.5};

        Stats<Double> dob = new Stats<Double>(darr);
        double w= dob.average();
        System.out.println(w);
        System.out.println(iob.SameAVG(dob));

    }    
}
