public public boolean isEligible(double gpa, int attendancePercent, boolean isDisciplinaryClear) {
    if (gpa > 3.5 && attendancePercent >= 90 && isDisciplinaryClear) {
      return true; 
    } else {
      return false; 
    }
  } Main {
    
}
