int singleNumber(int* nums, int numsSize){
    if (numsSize == 1) return nums[0];
    int ans = 0;
    for (int i = 0; i < numsSize; i++) ans ^= nums[i];
    return ans;
}