// Solution without using inbuilt functions
class Solution {
public:
    bool isPalindrome(string s) {
        string newString = "";
        for(char c:s){
            if((c >= 48 && c <= 57) || (c >= 65 && c <= 90) || (c >= 97 && c <= 122)){
                if(c >= 65 && c <= 90) newString += c + 32;
                else newString += tolower(c);
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
