public int close10(int a, int b) {
    int distA = Math.abs(a - 10);
    int distB = Math.abs(b - 10);

    if (distA < distB) {
        return a;
    } else if (distB < distA) {
        return b;
    } else {
        return 0;
    }
}
