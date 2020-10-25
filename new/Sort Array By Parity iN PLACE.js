/**
 * @param {number[]} A
 * @return {number[]}
 */
var sortArrayByParity = function(A) {

    function evensort(a, b){
        if (a%2 === 0 && b%2 === 0) return 0
        else if (a%2 === 0) return -1
        else if (b%2 === 0) return 1
    }
    A.sort(evensort)
    return A

};