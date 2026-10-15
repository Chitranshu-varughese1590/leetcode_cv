class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int n = nums.length;
        
        int sum = 0;
        for (int i = 0; i < k; i++) {
            sum += nums[i];
        }
        
        int maxSum = sum;
        int s = 0;
        int e = k;
        
        while (e < n) {
            sum = sum + nums[e] - nums[s];
            s++;
            
            if (sum > maxSum) {
                maxSum = sum;
            }
            
            e++;
        }
        
        return (double) maxSum / k;
    }
}