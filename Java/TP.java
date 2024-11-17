import java.util.*;
import java.io.*;


class filewrite1 extends Thread{
    @Override
    public void run(){
        byte b[] = {104,105,106,107,108,109,110,111,112,113,114,115};
        File obj = new File("file1.txt");
        try{
            FileOutputStream fout = new FileOutputStream(obj);
            System.out.println("Thread1 writing to file1");
            fout.write(b);
            fout.close();
        }
        catch(FileNotFoundException e){
            System.out.println("File not found");
        }
        catch(IOException e){
            System.out.println("IO exception");
        }
    }
}
class filewrite2 extends Thread{
    @Override
    public void run(){
        byte b[] = {11,12,17};
        File obj = new File("file1.txt");
        try{
            FileOutputStream fout = new FileOutputStream(obj);
            System.out.println("Thread2 writing to file1");
            fout.write(b);
            fout.close();
        }
        catch(FileNotFoundException e){
            System.out.println("File not found");
        }
        catch(IOException e){
            System.out.println("IO exception");
        }
    }
}
class TP{
    public static void main(String [] args){
        
        filewrite1 f1 = new filewrite1();
        filewrite2 f2 = new filewrite2();
        f2.setPriority(10);
        f1.setPriority(1);
        f1.start();
        f2.start();

    }
}

