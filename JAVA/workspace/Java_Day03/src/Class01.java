
public class Class01 {
	String name;
	int age;
	String hobby;

	public void info() {
		System.out.println("���� �̸��� " + name + "�Դϴ�.");
		System.out.println("���̴� " + age + "��, ��̴� " + hobby + "�Դϴ�.");
	}

	public void study(int time) {
		System.out.println(time + " ��ŭ ��������.");
	}
	
	// �޼��� �����ε�
	// �Ű������� Ÿ���� �ٸ��ų� ������ �ٸ��� �Ͽ� ������
	public void study(long time) {
		System.out.println(time + " ��ŭ ��������.");
	}
}
