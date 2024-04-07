class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int low = 0, high = 0, size = s.size(), windowSize, result = 0;
        unordered_map<char,int> letters;
        while(high < size){
            if(letters[s[high]] > 0) letters[s[high]]++;
            else letters[s[high]] = 1;
            windowSize = high - low + 1;
            if(letters.size() == windowSize) result = max(result, windowSize);
            else{
                while(letters.size() < windowSize){
                    if(--letters[s[low]] == 0) letters.erase(s[low]);
                    low++;
                    windowSize = high - low + 1;
                    }
                }
            high++;
    }
        return result;
        }
};