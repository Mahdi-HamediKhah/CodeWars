function solution(roman) {
  const romanValues = {
    I: 1,
    V: 5,
    X: 10,
    L: 50,
    C: 100,
    D: 500,
    M: 1000,
  };
  const romanArray = roman.split("");
  let result = romanArray.reduce((acc, cur, index, arr) => {
    if (index === 0) return romanValues[cur];
    if (romanValues[arr[index]] <= romanValues[arr[index - 1]]) {
      return acc + romanValues[cur];
    } else {
      return acc + romanValues[cur] - 2 * romanValues[arr[index - 1]];
    }
  }, 0);
  return result;
}
