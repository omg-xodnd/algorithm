/*
title : binary gap
about : iterations
date  : 2020.09.26
link  : https://app.codility.com/demo/results/trainingBSVTE9-BHA/
description :
  - find maximal sequence of zeros in binary
 */

/**
 * 
 * @param {Integer} N a random integer within range [1..2,147,483,647]
 * @returns {Integer} maxGap
 */
function solution(N) {
  const bin = N.toString(2)
  const L = bin.length
  
  console.log(bin)
  let maxGap = 0
  let nowGap = 0
  let i = 0
  while (i < L) {
      if (bin[i] === '0') {
          nowGap++
      } else {
          if (nowGap){
              maxGap = Math.max(maxGap, nowGap)
              nowGap = 0
          }
      }
      i++
  }
  return maxGap
}

console.log(solution(32))