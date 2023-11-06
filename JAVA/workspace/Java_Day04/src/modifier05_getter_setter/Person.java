package modifier05_getter_setter;

public class Person {
	private String name;
	private int age;
	private boolean hungry;

	// �����ڸ� �̿��ϸ� �ν��Ͻ� �������� �ʱ�ȭ �� �� �ִ�.
	public Person() {
		
	}
	
	public Person(String name, int age) {
		this.name = name;
		this.age = age;
	}
	
	// setter & getter
	// setter(������) : set���������
	public void setName(String name) {
		this.name = name;
	}
	
	// getter(������) : get���������
	public String getName() {
		return name;
	}

	public int getAge() {
		return age;
	}
	
	// �޼��带 �̿��ϸ� ������ ���� ������ �� �� �ְ� �ȴ�.
	public void setAge(int age) {
		if (age < 0 || age > 110) {
			System.out.println("�峭ġ����!");
			return;
		}
		this.age = age;
	}
	
	// boolean Ÿ���� getter�� is�� ����Ѵ�.
	public boolean isHungry() {
		return hungry;
	}

	public void setHungry(boolean hungry) {
		this.hungry = hungry;
	}
}
