class Solution {
    public List<Integer> diffWaysToCompute(String input) {
        List<Integer> res = new ArrayList<>();
        int len = input.length();
        for(int i = 0; i < len; i++){
            char c = input.charAt(i);
            if(c == '*' || c == '-' || c == '+'){
                List<Integer> left = diffWaysToCompute(input.substring(0, i));
                List<Integer> right = diffWaysToCompute(input.substring(i + 1, len));
                for(Integer l : left){
                    for(Integer r : right){
                        if(c == '*') res.add(l * r);
                        else if(c == '+') res.add(l + r);
                        else if(c == '-') res.add(l - r);
                    }
                }
            }
        }
        if(res.size() == 0) res.add(Integer.parseInt(input));
        return res;
    }
}
