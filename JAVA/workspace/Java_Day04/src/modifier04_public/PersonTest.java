package modifier04_public;

public class PersonTest {
	public static void main(String[] args) {
		Person p = new Person();
		// 다른 클래스, 같은 패키지
		// 아무거나 다 가능
		p.age = 10;
		p.name = "kim";
	}
}
