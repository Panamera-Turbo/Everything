class Solution{
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