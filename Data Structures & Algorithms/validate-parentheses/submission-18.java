class Solution {
    public boolean isValid(String s) {
        ArrayList<Character> paran_stack = new ArrayList<>();
        HashMap<Character, Character> paran_match = new HashMap<>();
        paran_match.put(')', '(');
        paran_match.put('}', '{');
        paran_match.put(']', '[');
        for (int i=0; i<s.length(); i++) {
            char l = s.charAt(i);
            if (paran_match.get(l) == null) {
                paran_stack.add(l);
            } else {
                if (paran_stack.size() == 0) {
                    return false;
                }
                char last_elem = paran_stack.get(paran_stack.size()-1);
                if (paran_match.get(l) == last_elem){
                    paran_stack.remove(paran_stack.size()-1);
                } else {
                    return false;
                }
            }
        }
        if (paran_stack.size() == 0) {
            return true;
        }
        return false;
    }
}
