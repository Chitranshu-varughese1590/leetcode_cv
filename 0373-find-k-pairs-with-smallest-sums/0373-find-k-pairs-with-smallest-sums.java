import java.util.*;

class Solution {
    public List<List<Integer>> kSmallestPairs(int[] nums1, int[] nums2, int k) {
        List<List<Integer>> result = new ArrayList<>();
        
        // Edge case check
        if (nums1.length == 0 || nums2.length == 0 || k == 0) {
            return result;
        }
        
        // Min-Heap tracking [index1, index2, sum] sorted by the sum (index 2)
        PriorityQueue<int[]> pq = new PriorityQueue<>(
            (a, b) -> Integer.compare(a[2], b[2])
        );
        
        // Initialize the heap with the first element of nums1 paired with nums2[0]
        // We only need to go up to min(nums1.length, k) elements
        for (int i = 0; i < Math.min(nums1.length, k); i++) {
            pq.offer(new int[]{i, 0, nums1[i] + nums2[0]});
        }
        
        // Extract the k smallest pairs
        while (k > 0 && !pq.isEmpty()) {
            int[] curr = pq.poll();
            int i = curr[0];
            int j = curr[1];
            
            // Add current pair values to the result list
            result.add(Arrays.asList(nums1[i], nums2[j]));
            k--;
            
            // If there's a next element in nums2 for the current nums1[i], push it to the heap
            if (j + 1 < nums2.length) {
                pq.offer(new int[]{i, j + 1, nums1[i] + nums2[j + 1]});
            }
        }
        
        return result;
    }
}