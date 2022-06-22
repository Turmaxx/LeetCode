int searchInsert(int* nums, int numsSize, int target){
    int left = 0;
    int right = numsSize - 1;
    int mid = 0;
    
    while (left < right){
        
        mid = left + (right - left) / 2;
    
        if (nums[mid] == target){
            return mid;
        }
        else if (nums[mid] < target){
            left = mid + 1;
        }
        else {
            right = mid;
        }
    }
    if (left == numsSize - 1 && nums[left] < target){
        return left + 1;
    }
    else{
        return left;
    }
}