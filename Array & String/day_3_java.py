public String backAround(String str) {
  // 1. Measure and find the last character index (Length - 1)
  int lastPos = str.length() - 1; 
  
  // 2. Cut the last character out
  String lastLetter = str.substring(lastPos); 
  
  // 3. Assemble the new string
  return lastLetter + str + lastLetter;
}