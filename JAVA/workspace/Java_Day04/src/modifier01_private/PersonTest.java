package modifier01_private;

public class PersonTest {
	public static void main(String[] args) {
		Person p = new Person();
		// Person�� PersonTest�� �ٸ� Ŭ���� �����̴�.
		
//		p.age �� p.name �� private�̹Ƿ� ���� �Ұ�
		p.info();
	}
}
