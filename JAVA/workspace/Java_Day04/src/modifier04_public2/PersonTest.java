package modifier04_public2;

import modifier04_public.Person;

public class PersonTest {
	public static void main(String[] args) {
		Person p = new Person();
		// 다른 클래스, 다른 패키지
		p.age = 10;
		p.name = "Kim";
	}
}
