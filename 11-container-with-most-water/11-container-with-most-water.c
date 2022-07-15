#define max_h(a,b) ((a < b)? b:a)
int maxArea(int* height, int heightSize){
    int maxArea = -1;
    int start = 0;
    int end = heightSize - 1;
    
    while (start < end){
        
        if (height[start] < height[end]){
            maxArea = max_h(maxArea, height[start] * (end - start));
            start++;
        }else{
            maxArea = max_h(maxArea, height[end] * (end - start));
            end--;
        }
    }
    
    return maxArea;
}