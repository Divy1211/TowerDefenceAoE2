mutable void appendInt(int arrayId = -1, int value = -1) {
    int size = xsArrayGetSize(arrayId);
    xsArrayResizeInt(arrayId, size + 1);
    xsArraySetInt(arrayId, size, value);
}

mutable void print(string msg = "") {
    static int lineNo = 1;
    string data = "L#" + lineNo + ": " + msg;
    xsChatData(data);
    lineNo++;
}
