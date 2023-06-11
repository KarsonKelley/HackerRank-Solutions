function plusMinus(arr) {
    // Write your code here
    let n = arr.length
    let z_count = 0, p_count = 0, n_count = 0;
    for(let i = 0; i < n; i++){
        if(arr[i] > 0){
            p_count++;
        }
        else if(arr[i] < 0){
            n_count++;
        }
        else{
            z_count++;
        }
    }
    console.log((p_count/n).toFixed(6));
    console.log((n_count/n).toFixed(6));
    console.log((z_count/n).toFixed(6));
}