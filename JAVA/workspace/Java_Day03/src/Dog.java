
public class Dog {
	String name;
	
	// �⺻ ������(�Ű����� X)
	// Ŭ������� �����ϰ� �ۼ�, �Ű����� X, ��ȯŸ�� X
	public Dog() {
		this("�⺻");
		System.out.println("�⺻������");
		// �⺻(default) ������ : Ŭ���� ���� �����ڰ� �ϳ��� ���ǵǾ� ���� ���� ���
		// JVM�� �ڵ����� �����ϴ� ������
	}
	

//	public Dog(String n) {
//		name = n;
//	}
	
	public Dog(String name) {
		this.name = name;
	}
}
