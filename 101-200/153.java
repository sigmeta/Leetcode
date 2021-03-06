public class Solution {
    public int findMin(int[] nums) {
        int low=0,high=nums.length-1,mid;
        while(low<high){
            mid=(low+high)/2;
            if(nums[mid]>nums[high])
                low=mid+1;
            else
                high=mid;
        }
        return nums[low];
    }
}
