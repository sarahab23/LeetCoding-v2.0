class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int low = 0, high = 0, windowSum = 0, result = INT_MAX, size = nums.size();
        while(high < size){
            windowSum += nums[high];
            while(windowSum >= target){
                result = min(result, high - low + 1);
                windowSum -= nums[low];
                low++;
                }
            high++;
            }
        return (result == INT_MAX? 0 : result);
    }
};