public class multirunmesage{
    public static void main(String[] args) throws InterruptedException {
        Thread thr1 = new Thread(new Runnable(){
            @Override
            public void run(){
                System.out.println("Hello");

            }
        });
        Thread thr2 = new Thread(new Runnable(){
            @Override
            public void run(){
                System.out.println("There");
            }
        });
        Thread thr3 = new Thread(new Runnable(){
            @Override
            public void run(){
                System.out.println("....how are you?");
            }
        });
        thr1.start();
        thr1.join();
        thr2.start();
        thr2.join();
        thr3.start();
        thr3.join();

    }
}