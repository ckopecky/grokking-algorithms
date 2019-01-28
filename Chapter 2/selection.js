const findSmallest = (arr) => {
    smallest = arr[0];
    smallest_index = 0;

    for(let i = 0; i < arr.length; i++){
        if(arr[i] < smallest){
            smallest = arr[i];
            smallest_index = i;
        }    
    }
    return smallest_index;
}

const selectionSort = (arr) => {
    let newArr = [];
    if(!arr.length) {
        return [];
    }
    for(let i = 0; i < arr.length; i++){
        let smallest = arr.splice( findSmallest( arr ), 1 );
        newArr.push(smallest);
        return smallest.concat( selectionSort( arr ) );

    }
    return newArr;
}

console.log(selectionSort([55, 323, 63, 2, 10]));