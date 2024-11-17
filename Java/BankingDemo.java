import java.util.*;

class InSufficientBalanceException extends Exception {
  InSufficientBalanceException(String s) {
    super(s);
  }
}

class Account {
  int AccountNumber;
  String name;
  double balance = 0.0;
  String address;

  public Account(int AccountNumber, String name, double balance, String address) {
    this.AccountNumber = AccountNumber;
    this.name = name;
    this.balance = balance;
    this.address = address;
  }

  public void deposit(double dep) {
    balance += dep;
  }

  public void withdraw(double amount) {
    try {
      check(amount);
    } catch (InSufficientBalanceException e) {
      System.out.println(e);
    }
    balance -= amount;

  }

  public void check(double amount) throws InSufficientBalanceException {
    if (balance - amount < 1000) {
      throw new InSufficientBalanceException("You do not have enough balance.");
    }
  }

  public double checkBalance() {
    return balance;
  }
}

class SavingAccount extends Account {
  double per;

  SavingAccount(int AccountNumber, String name, double balance, String address, double per) {
    super(AccountNumber, name, balance, address);
    this.per = per;
  }

  public double interest(double amount) {
    amount += amount * per;
    return amount;
  }

  @Override
  public void deposit(double amount) {
    amount = interest(amount);
    balance += amount;
  }

  @Override
  public void withdraw(double amount) {
    System.out
        .println("The following operation is not possible beacause The account you entered is a SAVINGS ACCOUNT.");

  }

}

public class BankingDemo {
  public static void main(String[] args) {
    Scanner inp = new Scanner(System.in);
    Account ac = new Account(123, "Srinivas", 14500, "Rampura,Udupi, Karnataka, 574118");
    while (true) {
      System.out.println("1.Deposit\n2.Withdraw\n3.Check Balance\n4.Exit");
      int ch = inp.nextInt();
      if (ch == 1) {
        System.out.println("Enter the amount to be deposited:");
        double amount = inp.nextDouble();
        ac.deposit(amount);
      } else if (ch == 2) {
        System.out.println("Enter the amount to be withdraw");
        double amount = inp.nextDouble();
        ac.withdraw(amount);
      } else if (ch == 3) {
        System.out.println("Balance amount in your account is:" + ac.checkBalance());
      } else {
        break;
      }
    }
    SavingAccount sac = new SavingAccount(456, "Kulal", 0, "vfgfgf", 5.2);
    while (true) {

      System.out.println("1.Deposit\n2.Withdraw\n3.Check Balance\n4.Exit");
      int ch = inp.nextInt();

      if (ch == 1) {
        System.out.println("Enter the amount to be deposited:");
        double amount = inp.nextDouble();
        sac.deposit(amount);
      } else if (ch == 2) {
        System.out.println("Enter the amount to be withdraw");
        double amount = inp.nextDouble();
        sac.withdraw(amount);
      } else if (ch == 3) {
        System.out.println("Balance amount in your account is:" + sac.checkBalance());
      } else {
        break;
      }
    }
    System.out.println("Done");
  }
}
