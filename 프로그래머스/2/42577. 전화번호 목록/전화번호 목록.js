function solution(phone_book) {
  const phone = new Set(phone_book);
  for (const number of phone_book) {
    for (let i = 1; i < number.length; i++) {
      if (phone.has(number.slice(0, i))) {
        return false;
      }
    }
  }

  return true;
}