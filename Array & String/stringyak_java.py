public String stringYak(String str) {
  String result = "";
  for (int i = 0; i < str.length(); i++) {
    if (i <= str.length() - 3 && str.charAt(i) == 'y' && str.charAt(i + 2) == 'k') i += 2;
    else result += str.charAt(i);
  }
  return result;
}