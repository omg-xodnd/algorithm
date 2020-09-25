/*
title : codility lesson 02 - cyclic rotation
about : Arrays
date  : 2020.09.26
link  : https://app.codility.com/demo/results/training8UF3ZB-77E/
description :
  - rotating an array K times
*/

/**
 * 
 * @param {Array} A an array
 * @param {Integer} K rotating counts
 * @returns {Array} result of rotation
 */
function solution(A, K) {
  const L = A.length
  const pointer = L - (K % L)
  const preA = A.slice(pointer)
  const postA = A.slice(0, pointer)
  return [...preA, ...postA]
}

A = [3, 8, 9, 7, 6]
K = 3
console.log(solution(A, K))