function solution(clothes) {
 const cloth = new Map();

  for (const [c, k] of clothes) {
    cloth.set(k, (cloth.get(k) || 0) + 1);
  }
  let answer = 1;
  for (const [_, count] of cloth) {
    answer *= count + 1;
  }
  return answer - 1;
}