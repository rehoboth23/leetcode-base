function solution(num){

    var count = 0
    const upper_limit = Math.ceil(Math.sqrt(2*num+0.25)-0.5)+1

    for(var i = 1; i < upper_limit; i++){
        if ((num - i *(i+1)/ 2)%i === 0) {
            count += 1
        }
    }
    return count
}

solution(15)
