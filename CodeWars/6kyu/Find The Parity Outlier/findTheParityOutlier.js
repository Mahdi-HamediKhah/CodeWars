function findOutlier(integers) {
  const even = [];
  const odd = [];
  integers.forEach((number) => {
    if (number % 2 == 0) {
      even.push(number);
    } else {
      odd.push(number);
    }
  });
  if (even.length == 1) {
    return even[0];
  } else {
    return odd[0];
  }
}
