class Solution {
public:
    int maxVowels(string s, int k) {
        int size = s.size(), result = 0, current = 0,x;
        for(int i = 0 ; i < size ; i++){
            if(s[i]=='a' || s[i]=='e' || s[i]=='i' || s[i]=='o' || s[i]=='u' ) current++;
            result = current > result ? current : result;
            if(result == k) break;
            if(i >= k-1){
                x = i - k + 1;
                if(s[x]=='a' || s[x]=='e' || s[x]=='i' || s[x]=='o' || s[x]=='u' ) current--;
            }
        }
        return result;
    }
};
