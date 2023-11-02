package jvm;

public class PersonTest {
	public static void main(String[] args) {
		Person p1 = new Person();
		p1.name = "Kim";
		
		p1.pCount = 10;
		System.out.println(p1.pCount);
		
		Person.pCount = 20;
		System.out.println(Person.pCount);
	}
}
