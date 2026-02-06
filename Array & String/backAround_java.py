public String backAround(String str) {
  
  int lastPos = str.length() - 1; 
  

  String lastLetter = str.substring(lastPos); 
  

  return lastLetter + str + lastLetter;
}
