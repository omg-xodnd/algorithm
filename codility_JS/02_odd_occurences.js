/*
title : odd occurences in array
about : Arrays
date  : 2020.09.26
link  : https://app.codility.com/demo/results/trainingQU36HX-E6C/
description :
  - find the element that has no pair with same value
  - used Object as dictionary
  - can be solved with XOR assignment(^=)
*/

/**
 * 
 * @param {Array} A an array
 * @returns {Number} the element with no pair
 */
function solution(A) {
  const counter = {}
  for (let num of A) {
    if (counter.hasOwnProperty(num)) {
      delete counter[num]
    } else {
      counter[num] = 1
    }
  }
  return Number(Object.keys(counter)[0])
}

A = [9, 3, 9, 3, 9, 7, 9]
console.log(solution(A))