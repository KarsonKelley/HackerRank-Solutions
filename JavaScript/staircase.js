function staircase(n) {
    // Write your code here
    let count = 0;
    for(let i = 0; i < n; i++){
        console.log(' '.repeat(n-(i+1))+ '#'.repeat(i+1))
    }
}