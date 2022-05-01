function sumArray(array){
    // input validation
    if ((array === null) || (array.length <= 1)){
        return 0;
    }
    let min = array[0];
    let max = array[0];
    let totalExcludingMinandMax = 0;
    let min_count = 0;
    let max_count = 0;


    for (let i = 0; i < array.length; i++){
        if (min > array[i]){
            min = array[i];
        }
        if (max < array[i]){
            max = array[i];
        }
    }
    
    for (let i = 0; i < array.length; i++){
        if (array[i] == min && min_count != 1){
            totalExcludingMinandMax += array[i];
            min_count = 1;
        }
        else if(array[i] == max && max_count != 1){
            totalExcludingMinandMax += array[i];
            max_count = 1;
        }
        else{
            if ((array[i] !== min) && (array[i] !== max)){
                totalExcludingMinandMax += array[i]
            }
        }
    }

    return totalExcludingMinandMax;

}

console.log( sumArray(null) ); // 0
console.log( sumArray([ ])  ); // 0
console.log( sumArray([ 3 ]) ); // 0
console.log( sumArray([ 3, 5 ]) ); // 0
console.log( sumArray([ 6, 2, 1, 8, 10 ]) ); // 16
console.log( sumArray([ 0, 1, 6, 10, 10 ]) ); // 17
console.log( sumArray([ -6, -20, -1, -10, -12 ]) ); // -28
console.log( sumArray([ -6, 20, -1, 10, -12 ]) ); // 3