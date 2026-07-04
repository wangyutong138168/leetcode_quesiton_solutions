public String minCat(String a, String b) {
    int len = Math.min(a.length(), b.length());
    return a.substring(a.length() - len) + b.substring(b.length() - len);
}
