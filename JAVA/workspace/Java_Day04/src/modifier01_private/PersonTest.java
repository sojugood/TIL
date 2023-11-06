package modifier01_private;

public class PersonTest {
	public static void main(String[] args) {
		Person p = new Person();
		// Person과 PersonTest는 다른 클래스 파일이다.
		
//		p.age 나 p.name 은 private이므로 접근 불가
		p.info();
	}
}
