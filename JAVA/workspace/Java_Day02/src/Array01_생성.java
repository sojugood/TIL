
public class Array01_���� {
	public static void main(String[] args) {
		// 1���� �迭�� �����ϴ� ���
		int[] score1; // �� ����� ����
		int score2[];

		// �迭�� �����ϴ� ���
		// 1. �ڷ���[] �̸� = new �ڷ���[����]; ���� �ڷ����� �ʱⰪ���� �ʱ�ȭ
		int[] score3 = new int[5]; // int���� �⺻���� 0�̴�.

		// 2. �ڷ���[] �̸� = new �ڷ���[]{1, 2, 3, 4};
		int[] score4 = new int[] { 1, 2, 3, 4 };

		// 3. �ڷ���[] �̸� = {1, 2, 3, 4}; // ����� ���ÿ� �ʱ�ȭ
		int[] score5 = { 1, 2, 3, 4 }; // �� ����� �ణ�� ��������� �ִ�.

		score3 = new int[6];
		score3 = new int[] { 1, 2, 3, 4, 5 };
//		score3 = {1, 2, 3, 4, 5}; // �̰� �ȵȴ�.
		
		int[] score6 = new int[5];
		
		score6[0] = 10;
		score6[1] = 20;
//		score6[5] = 60; // �ε��� ���� �ʰ�
	}
}
