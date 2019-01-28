const quicksort = (arr) => {
    let less = [];
    let more = [];
    let pivot = arr[0];
    if(arr.length < 2) {
        return arr;
    }
    else {
        for(let i = 1; i < arr.length; i++){
            if(arr[i] <= pivot) {
                less.push(arr[i]);
            }
            else {
                more.push(arr[i]);
            }
        }
        return quicksort(less).concat([pivot]).concat(quicksort(more));
    }
}

console.log(quicksort([10, 5, 22, 1952, 2, 3]));