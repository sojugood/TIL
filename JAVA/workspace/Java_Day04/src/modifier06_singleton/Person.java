package modifier06_singleton;

// Person이라고 하는 이 클래스를 싱글패턴을 적용하고 싶다.
public class Person {
	// 2. 내가 가지고는 있어야겠다.
	// 5. 이 변수도 static으로 선언해야 아래 메서드에서 리턴 가능
	private static Person instance = new Person();
	
	// 1. 외부에서 생성하지 못하게 막아라.
	// 		- 기본생성자를 작성하고 접근제한자를 private하게 만들어라.
	private Person() {
	}
	
	// 3. 외부에서 나의 instance를 가져다 쓸 수 있게끔 해줘야함.
	// 4. 외부에서 가져다 쓰기 위해 메모리에 미리 올려놓자. static
	public static Person getInstance() {
		// 2번에서 인스턴스 변수만 선언한 경우 아래 주석과 같이 작성해도 됨
//		if (instance == null) {
//			instance = new Person();
//		}
		return instance;
	}
}
