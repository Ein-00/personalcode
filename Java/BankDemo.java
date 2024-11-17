class Insufficient extends Exception{
    private double amount;
    public Insufficient(double amount){
        this.amount = amount;
    }
    public double getAmount(){
        return amount;
    }
}
class CheckingAccount{
    private double balance;
    private int number;
    public CheckingAccount(int number){
        this.number = number;
    }
    public void deposit(double amount){
        balance+= amount;
    }
    public void withdraw(double amount) throws Insufficient{
        if(amount <= balance){
            balance -= amount;
        }
        else{
            double needs = amount - balance;
            throw new Insufficient(needs);
        }

    }
    public double getBalance(){
        return balance;
    }
    
    public int getNumber(){
        return number;
    }
}
class BankDemo{
    public static void main(String[] args){
        CheckingAccount c = new CheckingAccount(101);
        System.out.println("Depositing Rs500");
        c.deposit(500);
        try{
            System.out.println("\n Withdrawing Rs100");
            c.withdraw(100.00);
            System.out.println("\nWithdrawing Rs600");
            c.withdraw(600.00);
        }
        catch(Insufficient e){
            System.out.println(e);
        }

        System.out.println("Exiting");
    }

}
