package modifier03_protected;

public class Person {
	// ���� ��Ű�� ���� ����, �ٸ� ��Ű���� ��� ������ ����
	protected String name;
	protected int age;
	
	public void info() {
		System.out.printf("�̸�: %s, ����: %d\n", name, age);
	}
}
