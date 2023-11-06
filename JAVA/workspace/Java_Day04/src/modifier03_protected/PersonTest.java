package modifier03_protected;

public class PersonTest {
	public static void main(String[] args) {
		Person p = new Person();
		// 다른 클래스이지만 같은 패키지
		// 속성 접근 가능
		
		p.age = 10;
		p.name = "Kim";
	}
}
