package modifier01_private;

public class Person {
	// private : �� Ŭ���� �������� ����� �� �ִ� ������
	private String name;
	private int age;
	
	// ���� �Ʒ� �Լ����� ���� ����
	public void info() {
		System.out.printf("�̸�: %s, ����: %d\n", name, age);
	}
}
