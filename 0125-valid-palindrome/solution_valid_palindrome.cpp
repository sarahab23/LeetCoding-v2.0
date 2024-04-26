class Solution {
public:
    bool isPalindrome(string s) {
        string newString = "";
        for(char c:s){
            if(isalnum(c)){
                newString += tolower(c);
            }
        }
        int size = newString.size();
        bool result = true;
        if(size < 2) return result;
        int i = 0, j = size - 1;
        while(j > i){
            if(newString[i++] != newString[j--]){
                result = false;
                break;
            }
        }
        return result;
    }
};
