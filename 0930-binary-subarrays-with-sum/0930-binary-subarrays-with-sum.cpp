class Solution {
public:
    int countSubarraysWithSum(vector<int>& nums, int goal){
        if(goal < 0) return 0;
        int result = 0, size = nums.size(), low = 0, high = 0;
        long long int sum = 0;
        while(high < size){
            sum += nums[high];
            while(sum > goal){
                sum -= nums[low];
                low++;
            }
            result += high - low + 1;
            high++;
        }
        return result;
    }
    int numSubarraysWithSum(vector<int>& nums, int goal) {
        return countSubarraysWithSum(nums, goal) - countSubarraysWithSum(nums, goal - 1);
    }
};