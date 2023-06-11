function compareTriplets(a, b) {
    let alice_sum = 0;
    let bob_sum = 0;
    for(let i = 0; i < a.length && b.length; i++){
        if (a[i] > b[i]){
            bob_sum++;
        }
        else if (a[i] < b[i]){
            alice_sum++;
        }
    }
    let scores = [bob_sum, alice_sum];
    return scores;
}