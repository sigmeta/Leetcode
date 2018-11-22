public class Solution {
    public int maxProduct(int[] nums) {
        if(nums.length==0) return 0;
        int min=nums[0],max=nums[0],result=nums[0],temp;
        for(int i=1;i<nums.length;i++){
            temp=max;
            max=Math.max(Math.max(max*nums[i],min*nums[i]),nums[i]);
            min=Math.min(Math.min(temp*nums[i],min*nums[i]),nums[i]);
            result=Math.max(max,result);
        }
        return result;
    }
}
