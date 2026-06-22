public String withoutX(String str) {
    int start = str.startsWith("x") ? 1 : 0;
    int end = str.endsWith("x") ? str.length() - 1 : str.length();
    return start > end ? "" : str.substring(start, end);
}
