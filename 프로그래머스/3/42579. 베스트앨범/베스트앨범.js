function solution(genres, plays) {
  const answer = [];
  const playCnt = plays.length;
  const genreTotal = new Map();
  const genrePerPlays = new Map();

  for (let i = 0; i < playCnt; i++) {
    genreTotal.set(genres[i], (genreTotal.get(genres[i]) || 0) + plays[i]);
    if (!genrePerPlays.has(genres[i])) genrePerPlays.set(genres[i], []);
    genrePerPlays.get(genres[i]).push([plays[i], i]);
  }
  sortedGenre = [...genreTotal].sort((a, b) => b[1] - a[1]);

  for (const list of genrePerPlays.values()) {
    list.sort((a, b) => b[0] - a[0]);
  }

  for (const sg of sortedGenre) {
    for (const gpp of genrePerPlays.get(sg[0]).slice(0, 2)) {
      answer.push(gpp[1]);
    }
  }
  return answer;
}