package modifier01_private;

public class Person {
	// private : 내 클래스 내에서만 사용할 수 있는 제한자
	private String name;
	private int age;
	
	// 따라서 아래 함수에서 접근 가능
	public void info() {
		System.out.printf("이름: %s, 나이: %d\n", name, age);
	}
}
