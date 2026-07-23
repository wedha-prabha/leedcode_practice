int uniqueXorTriplets(int* nums, int numsSize) {
    if (numsSize < 3) {
        return numsSize;
    }
    
    int bit_length = 0;
    int temp = numsSize;
    while (temp > 0) {
        bit_length++;
        temp >>= 1;
    }
    
    return 1 << bit_length;
}