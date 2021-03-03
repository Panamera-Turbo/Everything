import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;
import java.util.TreeMap;


class Solution {
    //78
    public List<List<Integer>> subsets(int[] nums) {
        // List list = new List<List>();
        
    }
    //215
    public int findKthLargest(int[] nums, int k) {
        Arrays.sort(nums);
        return nums[nums.length-k];
    }
    //53
    public int maxSubArray(int[] nums) {
        int ans = nums[0];
        int sum = 0;
        for(int x : nums){
            sum = Math.max(sum + x, x);
            ans = Math.max(sum, ans);
        }                           
        return ans;
    }
    
    //169
    //方法1
    private int randRange(Random rand, int min, int max) {
        return rand.nextInt(max - min) + min;
    }

    private int countOccurences(int[] nums, int num) {
        int count = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == num) {
                count++;
            }
        }
        return count;
    }

    public int majorityElement_methodOne(int[] nums) {
        Random rand = new Random();

        int majorityCount = nums.length / 2;

        while (true) {
            int candidate = nums[randRange(rand, 0, nums.length)];
            if (countOccurences(nums, candidate) > majorityCount) {
                return candidate;
            }
        }
    }

    //方法2
    public int majorityElement_methodTwo(int[] nums) {
        int more = nums[0];
        int counter = 0;
        int p = 0;

        while(p < nums.length){
            if(nums[p] == more){
                ++counter;
            }else if(counter > 0){
                --counter;
            }else{
                ++counter;
                more = nums[p];
            }
            p++;
        }

        return more;
    }
    //344
    public void reverseString(char[] s) {
        int i = 0, j = s.length-1;
        char ch;
        while(i <= j){
            ch = s[i];
            s[i] = s[j];
            s[j] = ch;
            i++;
            j--;
        }
    }
    //206
    class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }
    
    public ListNode reverseList(ListNode head) {
        if(head == null || head.next == null)return head;

        ListNode p = reverseList(head.next);

        head.next.next = head;
        head.next = null;
        
        return p;
    }
    //509
    public int fib(int n) {
        if(n == 0)return 0;
        return n == 1 ? 1 : fib(n-1) + fib(n - 2);
    }
    //1438
    public int longestSubarray(int[] nums, int limit) {
        TreeMap<Integer, Integer> map = new TreeMap<Integer, Integer>();
        int n = nums.length;
        int left = 0, right = 0;
        int ret = 0;
        while (right < n) {
            map.put(nums[right], map.getOrDefault(nums[right], 0) + 1);

            while (map.lastKey() - map.firstKey() > limit) {
                map.put(nums[left], map.get(nums[left]) - 1);

                if (map.get(nums[left]) == 0) {
                    map.remove(nums[left]);
                }
                left++;
            }

            ret = Math.max(ret, right - left + 1);
            right++;
        }
        return ret;
    }

    //1004
    public int longestOnes(int[] A, int K) {
        int left = 0, lsum = 0, rsum = 0;
        int ans = 0;
        for (int right = 0; right < A.length; ++right) {
            rsum += 1 - A[right];
            while (lsum < rsum - K) {
                lsum += 1 - A[left];
                ++left;
            }
            ans = Math.max(ans, right - left + 1);
        }
        return ans;
    }    

    //1456
    public boolean isVowel(char ch){
        if(ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u'){
                return true;
        }
        return false;
    }
    public int maxVowels(String s, int k) {
        char[] arr = s.toCharArray();
        int window = 0;
        int res = 0;

        int i = 0;
        while(i < k){
            if(isVowel(arr[i])){
                window++;
            }
            i++;
        }
        res = window;
        i = 0;

        while(i + k < arr.length){
            if(isVowel(arr[i])){
                window--;
            }
            if(isVowel(arr[i + k])){
                window++;
            }
            i++;
            res = Math.max(res, window);
        }

        return res;
    }
    //209
    public int minSubArrayLen(int target, int[] nums) {
        int res = 0;
        int window;

        for (int i = 1; i <= nums.length; i++) {
            window = 0;
            for (int k = 0; k < i; k++) {
                window += nums[k];
            }
            if(window >= target){
                return i;
            }
            for (int j = 0; i + j < nums.length; j++) {
                window = window - nums[j] + nums[i + j];
                if(window >= target){
                    return i;
                }
            }
        }

        return res;
    }

    //556
    public int[][] matrixReshape(int[][] nums, int r, int c) {
        int[][] res = new int[r][c];
        if(nums.length * nums[0].length != r * c){
            return nums;
        }

        int i=0, j= 0, ii = 0, jj = 0;

        while(ii < r){
            while(jj < c){
                if(j >= nums[0].length){
                    j = 0;
                    i++;
                }
                
                res[ii][jj] =  nums[i][j];
                
                j++;
                jj++;
            }
            jj = 0;
            ii++;
        }

        return res;
    }
}


public class leetcodeTry{
    public static void main(String[] args) {
        return;
    }
}