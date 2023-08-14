public class MainApplication{
	public static void main(String[] args){
		Dog dog = new Dog();

		dog.name = "Tiger";
		dog.age = "2";
		dog.bark();
		dog.eat();
		dog.run();

		Cat cat = new Cat();
		cat.name = "some cat";
		cat.eat();

		Cat cat1 = new Cat();
		cat1.name = "Random Cat";
		cat1.eat();

		Cat cat2 = new Cat();
		cat2.name= "Black Cat";
		cat2.eat();

		cat2.meow();
		

	}
}
