import java.util.Arrays;

public class Array04_�迭�Ǻ��� {
	public static void main(String[] args) {
		int[] nums = { 42, 5, 3, 7, 23, 15 };
		// �迭 ����

		// �������� ������
		int[] tmp = new int[nums.length * 2];
		for (int i = 0; i < nums.length; i++) {
			tmp[i] = nums[i];
		}
		System.out.println(Arrays.toString(tmp));

		// Arrays.copyOf(�����迭, ������ �迭�� ũ��)
		int[] tmp2 = Arrays.copyOf(nums, nums.length * 2);
		System.out.println(Arrays.toString(tmp2));

		// System.arraycopy(�����迭, �����迭������, ����迭, ����迭������, ������ũ��)
		int[] tmp3 = new int[nums.length * 2];
		System.arraycopy(nums, 0, tmp3, 0, nums.length);
		System.out.println(Arrays.toString(tmp3));
	}
}
