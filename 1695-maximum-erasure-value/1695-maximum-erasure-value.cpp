class Solution {
public:
    int maximumUniqueSubarray(vector<int>& nums) {
        int size = nums.size(), low = 0, high = 0, result = INT_MIN, windowSize, windowScore = 0;
        unordered_map<int,int> uniqueElts;
        while(high < size){
            if(uniqueElts[nums[high]] > 0) uniqueElts[nums[high]]++;
            else uniqueElts[nums[high]] = 1;
            windowScore += nums[high];
            windowSize = high - low + 1;
            if(uniqueElts.size() == windowSize) result = max(result, windowScore);
            else{
                while(uniqueElts.size() < windowSize){
                    if(--uniqueElts[nums[low]] == 0) uniqueElts.erase(nums[low]);
                    windowScore -= nums[low];
                    low++;
                    windowSize--;
                    }
                }
            high++;
            }
        return result;
    }
};