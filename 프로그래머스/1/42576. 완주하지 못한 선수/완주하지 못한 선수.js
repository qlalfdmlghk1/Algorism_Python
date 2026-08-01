function solution(participant, completion) {
  const par = new Map();
  for (const p of participant) {
    par.set(p, (par.get(p) || 0) + 1);
  }

  for (const c of completion) {
    if (par.get(c)) {
      par.set(c, par.get(c) - 1);
    }
  }

  for (const [k, v] of par) {
    if (v != 0) {
      return k;
    }
  }
}
