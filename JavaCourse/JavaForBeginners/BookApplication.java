import java.util.Scanner;

public class BookApplication{

	public static void main(String[] args){
		System.out.println("Welcome to book store");
		System.out.println("Press 1 to Continue");
		System.out.println("Press any other number to exit");

		Scanner sc = new Scanner(System.in);
		int availableBooks = 10;
		double price = 20.22;
		boolean continueToMenu = true;
		if(sc.nextInt() == 1 ){

		while(continueToMenu){
			System.out.println("Number of books available :: " + availableBooks + " price per book " 
				+ price);
			System.out.println("Enter the number of books you want to buy");
			int booksToBuy = sc.nextInt();
			System.out.println("Enter your account balance");
			double balance = sc.nextDouble();

			double totalPrice = booksToBuy * price;

			while(totalPrice > balance){
				System.out.println("Your balance is not sufficient.");
				System.out.println("Enter balance that is equal or more than :: " + totalPrice);
				balance = sc.nextDouble();
			}

			if(totalPrice <= balance){
				availableBooks = availableBooks -booksToBuy;
				System.out.println("Your order is successful");
			}
			if(availableBooks < 1){
				continueToMenu = false;
				System.out.println("Shop is out of books. Closing for now");
			}	
		}

		}else{
			System.out.println("See you again. Bye");
			System.exit(0);
		}

	}
}