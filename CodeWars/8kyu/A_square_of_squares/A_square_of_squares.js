//Solution
let isSquare = function (n) {
  if (n >= 0) {
    if (Math.sqrt(n) % 1 === 0) {
      return true;
    } else {
      return false;
    }
  } else {
    return false; // fix me
  }
};
