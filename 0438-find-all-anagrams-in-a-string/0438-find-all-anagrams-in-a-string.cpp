class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        int k = p.size(), size = s.size();
        if(k > size) return vector<int>();
        vector<int> goal(26), current(26), result;
        for(char c:p) goal[c - 'a']++;
        for(int i = 0; i < size; i++){
            current[s[i] - 'a']++;
            if(i >= k - 1){
                if(goal == current) result.push_back(i - k + 1);
                current[s[i - k + 1] - 'a']--;
            }
        }
        return result;
    }
};