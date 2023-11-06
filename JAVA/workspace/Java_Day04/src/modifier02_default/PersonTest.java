package modifier02_default;

public class PersonTest {
	public static void main(String[] args) {
		Person p = new Person();
		// Person과 PersonTest는 다른 클래스이지만 같은 패키지
		
		// 속성 접근 가능
		p.age = 10;
		p.name = "Kim";
	}
}
