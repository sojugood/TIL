package modifier02_default;

public class Person {
	// 접근제한자를 생략하면, default
	String name;
	int age;
	
	public void info() {
		System.out.printf("이름: %s, 나이: %d\n", name, age);
	}
}
