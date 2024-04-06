class Solution {
public:
    int findSubarrays(vector<int>& nums, int k){
        int low = 0, high = 0, count = 0, result = 0, size = nums.size();
        while(high < size){
            count += nums[high];
            while(count > k){
                count -= nums[low];
                low++;
            }
            result += high - low + 1;
            high++;
        }
        return result;
    }
    int numberOfSubarrays(vector<int>& nums, int k) {
        int size = nums.size();
        vector<int> integers(size);
        for(int i = 0; i < size; i++){
            if(nums[i] % 2 == 0) integers[i] = 0;
            else integers[i] = 1;
        }
        return findSubarrays(integers, k) - findSubarrays(integers, k - 1);
    }
};