function queueTime(customers, n) {
  const tills = new Array(n).fill(0);
  for (const customer of customers) {
    let minIndex = tills.indexOf(Math.min(...tills));
    tills[minIndex] += customer;
  }
  return Math.max(...tills);
}

queueTime([2, 2, 3, 3, 4, 4], 2);
