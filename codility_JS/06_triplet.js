A = [ -3, 1, 2, -2, 5, 6 ]

function solution(A) {
  const sortedA = [...A].sort()
  console.log(sortedA)
  A.sort()
}

solution(A)
console.log(A)