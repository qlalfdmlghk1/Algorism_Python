function solution(genres, plays) {
  var answer = [];
  const musics = new Map();
  const genre_total = new Map();
  const total_music = genres.length;
  for (let i = 0; i < total_music; i++) {
    musics.set(genres[i], (musics.get(genres[i]) || 0) + plays[i]);
    genre_total.set(genres[i], [...(genre_total.get(genres[i]) || []), [plays[i], i]]);
  }

  const sorted_music = new Map([...musics].sort((a, b) => b[1] - a[1]));

  for (const list of genre_total.values()) {
    list.sort((a, b) => b[0] - a[0]); // 재생수 내림차순
  }

  for (const [genre] of sorted_music) {
    const list = genre_total.get(genre);
    for (const [, idx] of list.slice(0, 2)) {
      answer.push(idx);
    }
  }

  return answer;
}