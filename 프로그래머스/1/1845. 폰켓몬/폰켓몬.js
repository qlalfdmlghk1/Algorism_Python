function solution(nums) {
  pocketmon = new Map();

  for (const n of nums) {
    pocketmon.set(n, (pocketmon.get(n) || 0) + 1);
  }

  get = nums.length / 2;
  answer = Math.min(pocketmon.size, get);
  return answer;
}