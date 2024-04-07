class Solution {
public:
    int countGoodSubstrings(string s) {
        int low = 0, high = 0, size = s.size(), result = 0;
        unordered_map<char,int> letters;
        while(high < size){
            letters[s[high]]++;
            if(high - low + 1 < 3){
                high++;
            }
            else{
                if(letters.size() == 3) result++;
                if(--letters[s[low]] == 0) letters.erase(s[low]);
                low++;high++;
            }
        }
        return result;
    }
};