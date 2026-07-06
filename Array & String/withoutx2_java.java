public String withoutX2(String str) {
    if (str.length() < 2) return str.replace("x", "");
    return (str.charAt(0) == 'x' ? "" : str.substring(0, 1))
         + (str.charAt(1) == 'x' ? "" : str.substring(1, 2))
         + str.substring(2);
}
