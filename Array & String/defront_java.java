public String deFront(String str) {
    return (str.startsWith("a") ? "a" : "")
        + (str.length() > 1 && str.charAt(1) == 'b' ? "b" : "")
        + (str.length() > 2 ? str.substring(2) : "");
}
