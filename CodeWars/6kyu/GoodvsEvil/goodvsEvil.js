function goodVsEvil(good, evil) {
  let goodArmy = good.split(/\s+/);
  let evilArmy = evil.split(/\s+/);
  const goodworth = [1, 2, 3, 3, 4, 10];
  const evilworth = [1, 2, 2, 2, 3, 5, 10];
  const goodResult = goodArmy.reduce((acc, cur, index, arr) => {
    return acc + Number(cur) * goodworth[index];
  }, 0);
  const evilResult = evilArmy.reduce((acc, cur, index, arr) => {
    return acc + Number(cur) * evilworth[index];
  }, 0);

  return goodResult > evilResult
    ? "Battle Result: Good triumphs over Evil"
    : goodResult < evilResult
    ? "Battle Result: Evil eradicates all trace of Good"
    : "Battle Result: No victor on this battle field";
}


// const goodVsEvil = (g, e) => {
//   const w = [[1, 2, 3, 3, 4, 10], [1, 2, 2, 2, 3, 5, 10]];
//   const s = (a, v) => a.split(/\s+/).reduce((t, c, i) => t + c * v[i], 0);
//   const [G, E] = [s(g, w[0]), s(e, w[1])];
//   return G > E ? "Battle Result: Good triumphs over Evil" :
//          G < E ? "Battle Result: Evil eradicates all trace of Good" :
//                  "Battle Result: No victor on this battle field";
// };
