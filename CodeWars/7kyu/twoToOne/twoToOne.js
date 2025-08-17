function longest(s1, s2) {
  const str = s1 + s2;
  return str
    .split("")
    .sort()
    .filter((value, i, arr) => arr.indexOf(value) === i)
    .join("");
}

// function longest(s1, s2) {
//   return [...new Set(s1 + s2)].sort().join("");
// }
