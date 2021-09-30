//ebh3kpz
//Ellen Herrera
class Solution {
   public int removeDuplicates(int[] nums) {
        int lastInd = 0;
        
        if(nums.length == 0)
            return 0;
        if(nums.length == 1)
            return 1;
        
        for(int z = 0; z < nums.length-1; z++){
            if((nums[z] != nums[z+1])){
                nums[++lastInd] = nums[z+1]; 
            }
        }
        return lastInd+1;
    }
}