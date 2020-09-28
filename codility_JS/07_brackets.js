/*
title : brackets
about : Stack
date  : 2020.09.26
link  : https://app.codility.com/demo/results/trainingS9AZUZ-HSF/
description :
  - check if parenthesis is correctly nested
  - stack and ASCII code
*/

/**
 * 
 * @param {String} S an string has only parenthesis
 * @returns {Number} correct ? 1 : 0
 */
function solution(S) {
  const stack = []
  for (let brace of S) {
    const charCode = brace.charCodeAt()
    const diff = charCode - stack[stack.length-1]
    if (stack.length && (diff === 1 | diff === 2)) {
      stack.pop()
    } else {
      stack.push(charCode)
    }
  }
  return stack.length ? 0 : 1
}

S = '([)()]'
console.log(solution(S))
