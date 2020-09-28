/*
title : passing cars
about : prefix sums
date  : 2020.09.26
link  : https://app.codility.com/demo/results/trainingNV9UVQ-F75/
description :
  - Count the number of passing cars on the road.
*/

/**
 * 
 * @param {Array} A an array with car info
 * @returns {Number} the number of pairs of cars that passed each other
 */
function solution(A) {
  let count = 0
  let d = 0
  for (let car of A) {
      if (car === 0) {
          d++
      } else {
          count += d
      }
      if (count > 1000000000) {
          count = -1
          break
      }
  }
  return count
}