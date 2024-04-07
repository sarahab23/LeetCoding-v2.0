class Solution {
public:
    int findNiceSubarrays(vector<int>& nums, int k){
        int low = 0, high = 0, count = 0, result = 0, size = nums.size();;
        while(high < size){
            count += nums[high] % 2;
            while(count > k){
                count -= nums[low] % 2;
                low++;
            }
            result += high - low + 1;
            high++;
        }
        return result;
    }
    int numberOfSubarrays(vector<int>& nums, int k) {
        return findNiceSubarrays(nums, k) - findNiceSubarrays(nums, k - 1);
    }
};