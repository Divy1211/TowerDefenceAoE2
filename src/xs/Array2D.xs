mutable int arrayCreate2d(int width = 0, int height = 0) {
    int arrayId = xsArrayCreateInt(height);

    for(i = 0; < xsArrayGetSize(arrayId)) {
        xsArraySetInt(arrayId, i, xsArrayCreateInt(width));
    }

    return (arrayId);
}

mutable int arrayGet2d(int arrayId = -1, int x = 0, int y = 0) {
    int v = xsArrayGetInt(xsArrayGetInt(arrayId, y), x);
    return (xsArrayGetInt(xsArrayGetInt(arrayId, y), x));
}

mutable int arraySet2d(int arrayId = -1, int x = 0, int y = 0, int value = 0) {
    return (xsArraySetInt(xsArrayGetInt(arrayId, y), x, value));
}