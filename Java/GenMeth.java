
class GenMeth {
    static <T extends Comparable<T>,V extends T> boolean IsIn(T x, V[] y){
        for(int i = 0;i<y.length;i++){
            if(x.equals(y[i])){
                return true;
            }
           
        }
        return false;
    }
    public static void main(String[] args){
        Integer n[] = {1,2,3,4,5,6};
        if(IsIn(2, n)){
            System.out.println("2 is in nums");
        }
        if(!IsIn(7, n)){
            System.out.println("7 is not in the nums");
        }
        String strs[] = {"one", "two", "three","four","five"};
        if(IsIn("four", strs)){
            System.out.println("4 is in string.");
        }
        //The following give you a error as "four " can't be compared with int array.
        // if(IsIn("four", n)){
        //     System.out.println("4 is in string.");
        // }

    }
    
}
