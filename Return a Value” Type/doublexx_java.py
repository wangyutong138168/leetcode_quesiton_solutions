public boolean doubleX(String str) {
  int i = str.indexOf("x");
  if (i == -1 || i == str.length() - 1) return false;
  return str.charAt(i + 1) == 'x';
}