import java.util.Arrays;

public class Array03_�迭�Ǽ�ȸ {
	public static void main(String[] args) {
		int[] nums = { 42, 5, 3, 7, 23, 15 };

		// �ݺ����� ���� ��ȸ
//		for (int i = 0; i < nums.length; i++) {
//			System.out.println(nums[i]);
//		}

		// for-each
		// �������� ���� for��
//		for (�ڷ��� ������ : �ݺ��� �� �ִ� ��) {
//			
//		}
//		for (int n : nums) {
//			System.out.println(n);
//		}

		// �б�(��ȸ)�� ����, ���� �Ұ�
//		for (int x : nums) {
////			x = x * 2;
//			x *= 2;
//		}
//		
//		for (int x : nums) {
//			System.out.println(x);
//		}
//		
		for (int i = 0; i < nums.length; i++) {
			nums[i] *= 2;
		}

		for (int x : nums) {
			System.out.println(x);
		}

		// �迭���� ���� �ñ��� �� ����ϸ� �ٷ� �� �� ����
		System.out.println(Arrays.toString(nums));
	}
}
