package java01;

public class intro01_Hello {
	// crtl + space : �ڵ��ϼ�
	public static void main(String[] args) {
		// sysout
		System.out.println("Hello SSAFY!!");
		
		// println�� �ٹٲ�(new Line) ����
		System.out.print("Hello SSAFY!!");
		System.out.println("Hello SSAFY!!");
		
		// print("\n")�ϸ� �ٹٲ�
		System.out.print("Hello SSAFY!!");
		System.out.print("\n");
		System.out.print("Hello SSAFY!!\n");
		System.out.println("Hello SSAFY!!");
		
		// printf
		System.out.printf("%s\n", "Hello World!!");
		System.out.printf("%c\n", 'W');
		// 4ĭ�� Ȯ���� �� �����ʺ���
		System.out.printf("%4d\n", 10);
		// 4ĭ�� Ȯ���� �� ���ʺ���
		System.out.printf("%-4d\n", 10);
		// 4ĭ�� Ȯ���� �� �����ʺ���(��ĭ�� 0����)
		System.out.printf("%04d\n", 10);
		// �Ǽ�
		System.out.printf("%f\n", 10.1);
		// �Ǽ�(�Ҽ��� ��°�ڸ�����)(��°�ڸ����� �ݿø�)
		System.out.printf("%.2f\n", 10.105);

	}
}
