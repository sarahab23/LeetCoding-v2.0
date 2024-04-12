class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        vector<int> result;
        int current, nextGreaterNum, i, j, size = nums.size();
        bool found;
        for(i = 0; i < size; i++){
            found = false;
            current = nums[i];
            nextGreaterNum = -1;
            for(j = i + 1; j < size; j++){
                if(nums[j] > current){
                    nextGreaterNum = nums[j];
                    found = true;
                    break;
                }
            }
            if(found == false){
                for(j = 0; j < i; j++){
                    if(nums[j] > current){
                        nextGreaterNum = nums[j];
                        found = true;
                        break; 
                    }
                }
            }
            result.push_back(nextGreaterNum);
        }
        return result;
    }
};